from prettytable import PrettyTable
from copy import deepcopy
from conversions import determinize

class FiniteAutomata:
    def __init__(self, trans=None, initial="0", accepting=None, states=None, alphabet=None):
        self.trans = {}
        self.initial = initial
        self.accepting = set()
        self.states = set()
        self.alphabet = set()

    def return_constructor_recipe(self):
        return {
            'trans':     self.trans,
            'initial':   self.initial,
            'accepting': self.accepting,
            'states':    self.states,
            'alphabet':  self.alphabet,
        }

    def addTrans(self, from_, by, to):
        if from_ not in self.trans:
            self.trans[from_] = {}
        self.trans[from_][by] = to

    def addState(self, state):
        self.states.add(state)

    def addAccepting(self, state):
        self.accepting.add(state)

    def load(self, file):
        f = open(file, "r")
        f1 = f.readlines()
        initial = f1[1].replace('\n', '')
        accepting = f1[2].replace('\n', '').split(',')
        for s in accepting:
            self.addAccepting(s)

        alphabet = f1[3].replace('\n', '').split(',')
        for a in alphabet:
            self.alphabet.add(a)

        for line in f1[4:]:
            l1 = line.replace('\n', '').split(',')
            from_ = l1[0]
            by = l1[1]
            to = l1[2]

            self.addState(to)
            self.addState(from_)

            self.addTrans(from_, by, to)
        self.initial = initial

        for s in self.states:
            if s not in self.trans:
                self.trans[s] = {}
        return self

    def recognizes(self, word):
        current = self.initial
        for c in word:
            if c not in self.trans[current]:
                return False
            else:
                current = self.trans[current][c]

        return current in self.accepting

    def save(self, filename):
        with open(filename, "w") as writer:
            writer.write(str(len(self.states))+"\n")
            writer.write(self.initial+"\n")
            writer.write(str(",".join(sorted(self.accepting)))+"\n")
            writer.write(str(",".join(sorted(self.alphabet)))+"\n")

            for t in self.trans:
                for b in self.trans[t]:
                    writer.write("{},{},{}".format(t, b, self.trans[t][b]+"\n"))

    def show(self):
        for state in self.trans:
            aux1 = ""
            if state in self.accepting:
                aux1 += "*"
            if state == self.initial:
                aux1 += "->"
            for symbol in self.trans[state]:
                aux2 = aux1 + "transição({0}; {1}) = ".format(state, symbol)
                state_list = self.trans[state][symbol]

                formatted_state_list = ", ".join(state_list)
                if len(state_list) == 0:
                    continue
                else:
                    finalprint = aux2 + formatted_state_list

                print(finalprint)

    def union(self, other):
        result = NDFiniteAutomata()
        startState = "q0"
        result.addState(startState)
        result.initial = startState
        result.alphabet = self.alphabet
        result.alphabet.add("&")
        id = 1
        mapping = {}
        for state in sorted(list(self.states)):
            mapping[state] = "q" + str(id)
            result.addState(mapping[state])
            id += 1
        for state in sorted(list(self.states)):
            for a in self.alphabet:
                if a in self.trans[state].keys():
                    to = self.trans[state][a]
                    if isinstance(to, str):
                        result.addTrans(mapping[state], a, mapping[to])
                    else:
                        for s in to:
                            result.addTrans(mapping[state], a, mapping[s])
        for accept in self.accepting:
            result.addAccepting(mapping[accept])
        result.addTrans(startState, "&", mapping[self.initial])
        mapping = {}
        result.alphabet.update(other.alphabet)
        for state in sorted(list(other.states)):
            mapping[state] = "q" + str(id)
            result.addState(mapping[state])
            id+=1
        for state in sorted(list(other.states)):
            for a in other.alphabet:
                if a in other.trans[state]:
                    to = other.trans[state][a]
                    if isinstance(to, str):
                        result.addTrans(mapping[state], a, mapping[to])
                    else:
                        for s in to:
                            result.addTrans(mapping[state], a, mapping[s])
        for accept in other.accepting:
            result.addAccepting(mapping[accept])
        result.addTrans(startState, "&", mapping[other.initial])
        return result

    def complement(self):
        newAccepting = set()
        for s in self.states:
            if s not in self.accepting:
                newAccepting.add(s)
        self.accepting = newAccepting

    def intersection(self, other):
        self.complement()
        other.complement()
        AF = self.union(other)
        AF.complement()
        if AF.initial in AF.accepting:
            AF.accepting.remove(AF.initial)

        return AF

    def __eq__(self, other):
        return all([
            self.trans     == other.trans,
            self.initial   == other.initial,
            self.accepting == other.accepting,
            self.states    == other.states,
            self.alphabet  == other.alphabet,
    ])

class NDFiniteAutomata(FiniteAutomata):

    def addTrans(self, from_, by, to):
        if from_ not in self.trans:
            self.trans[from_] = {}
        if by not in self.trans[from_]:
            self.trans[from_][by] = set()
        self.trans[from_][by].add(to)

    def eClosure(self, states):
        eClosure = set()
        accept = False
        while states:
            s = states.pop()
            eClosure.add(s)
            if s in self.accepting:
                accept = True
            if "&" in self.trans[s]:
                for x in self.trans[s]["&"]:
                    if x not in eClosure:
                        states.append(x)
        return (eClosure, accept)

    def load(self, filename):
        f = open(filename, "r")
        f1 = f.readlines()
        initial = f1[1].replace('\n', '')
        accepting = f1[2].replace('\n', '').split(',')
        for s in accepting:
            self.addAccepting(s)

        alphabet = f1[3].replace('\n', '').split(',')
        for a in alphabet:
            self.alphabet.add(a)

        for line in f1[4:]:
            l1 = line.replace('\n', '').split(',')
            from_ = l1[0]
            by = l1[1]
            to = l1[2]

            if "-" in l1[2]:
                to = l1[2].split("-")
                for s in to:
                    self.addState(s)
                    self.addTrans(from_, by, s)
            else:
                self.addState(to)
                self.addState(from_)
                self.addTrans(from_, by, to)


        for s in self.states:
            if s not in self.trans:
                self.trans[s] = {}

        self.initial = initial
        return self

    def save(self, filename):
        with open(filename, "w") as writer:
            writer.write(str(len(self.states))+"\n")
            writer.write(self.initial+"\n")
            writer.write(str(",".join(sorted(self.accepting)))+"\n")
            writer.write(str(",".join(sorted(self.alphabet)))+"\n")

            for t in self.trans:
                for b in self.trans[t]:
                        f = '-'.join(self.trans[t][b])
                        writer.write("{},{},{}".format(t, b, f)+"\n")

    def recognizes(self, word):
        AF = FiniteAutomata()
        AF = determinize(self)
        return AF.recognizes(word)
