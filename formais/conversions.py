from formais.finite_automata import *
from formais.regular_expressions import *

from collections import defaultdict
import copy

def GR_to_AFND(GR):
    AFND = NDFiniteAutomata()

    AFND.states = GR.non_terminals.union('F')
    AFND.alphabet = GR.terminals
    AFND.initial = GR.initial_state

    if '&' in GR.rules[GR.initial_state]:
        AFND.accepting.add('&')
    AFND.accepting.add('F')

    trans = defaultdict(dict)
    for head, body in GR.rules.items():
        for symbol in body:
            if len(symbol) == 1 and symbol in GR.terminals:
                for accept in AFND.accepting:
                    if symbol not in trans[head]:
                        trans[head][symbol] = {accept}
                    else:
                        trans[head][symbol].add(accept)
            else:
                if symbol[0] not in trans[head]:
                    trans[head][symbol[0]] = {symbol[1]}
                else:
                    trans[head][symbol[0]].add(symbol[1])
    for symbol in AFND.alphabet:
        trans['F'][symbol] = 'Ø'

    AFND.trans = dict(trans)

    return AFND


def minimize(AFD):

    unreachable = set()
    reachable_all = set(AFD.initial)
    visited = set()
    unvisited = set(AFD.trans[AFD.initial].values())
    while unvisited:
        reachable = unvisited.pop()
        reachable_all.add(reachable)
        if reachable not in visited:
            unvisited.update(set(AFD.trans[reachable].values()))
            visited.add(reachable)
    unreachable = AFD.states - reachable_all - {AFD.initial}
    for state in unreachable:
        del AFD.trans[state]
    AFD.accepting = AFD.accepting - unreachable
    AFD.states = AFD.states - unreachable

    reach_all = AFD.accepting
    reachable = set()
    visited = set()
    while reach_all:
        next_reach_all = set()
        for state, trans_next in AFD.trans.items():
            for reach in reach_all:
                if reach in trans_next.values():
                    reachable.add(state)
                    if reach not in visited:
                        next_reach_all.add(state)
        visited.update(reach_all)
        reach_all = next_reach_all
    unreachable = AFD.states - reachable - AFD.accepting
    for state in unreachable:
        del AFD.trans[state]
    AFD.accepting = AFD.accepting - unreachable
    AFD.states = AFD.states - unreachable

    equivalencies = []
    equivalencies.append(AFD.accepting)
    equivalencies.append(AFD.states - AFD.accepting)
    next_equivalencies = []
    equivalencies_control = equivalencies[:]
    while True:
        for char in AFD.alphabet:
            equivalencies_prev = []
            for equivalent in equivalencies:
                goes_to_index = defaultdict(set)
                for state in equivalent:
                    n_equivalencies = len(equivalencies)
                    goes_to = AFD.trans[state].get(char, n_equivalencies)

                    if goes_to == n_equivalencies:
                        goes_to_index[n_equivalencies].add(state)
                    for i in range(len(equivalencies)):
                        if goes_to in equivalencies[i]:
                            goes_to_index[i].add(state)
                            break
                    else:
                        goes_to_index[n_equivalencies].add(state)
                for new_equivalence in goes_to_index.values():
                    equivalencies_prev.append(new_equivalence)
            equivalencies = equivalencies_prev
        if equivalencies_control == equivalencies:
            break
        equivalencies_control = equivalencies

    mapping = {}
    i = 0
    while equivalencies:
        char = 'c' + str(i)
        mapping[char] = equivalencies.pop()
        i += 1
    print('Mapeamento:', mapping)

    trans = defaultdict(dict)
    initial = ''
    accepting = set()

    for map_char, states in mapping.items():
        state = next(iter(states))
        if state in AFD.accepting:
            accepting.add(map_char)
        if state == AFD.initial:
            initial = map_char
        for char in AFD.alphabet:
            goes_to = AFD.trans[state].get(char)
            if goes_to:
                for map_char_aux, states_aux in mapping.items():
                    if goes_to in states_aux:
                        trans[map_char][char] = map_char_aux

    AFD_min = FiniteAutomata()
    AFD_min.trans = trans
    AFD_min.initial = initial
    AFD_min.accepting = accepting
    AFD_min.states = mapping.keys()
    AFD_min.alphabet = AFD.alphabet

    return AFD_min

def getState(l):
    if len(l) > 1:
        l = list(l)
        l.sort()
        return ''.join(l)
    else:
        return list(l)[0]

def determinize(input_AFND):
    AF = FiniteAutomata()
    AFND = copy.deepcopy(input_AFND)

    AF.initial = AFND.initial
    alph = AFND.alphabet

    if "&" in alph:
        AF.alphabet = alph.remove("&")
    else:
        AF.alphabet = alph
    AF.alphabet = AFND.alphabet
    tState = []
    AF.initial = AFND.initial

    for state in AFND.states:
        tState.append({state})
    while tState:
        stateList = list(tState.pop())
        init = False
        if len(stateList) == 1 and stateList[0] == AFND.initial:
            init = True
        (stateClosure, isAccepting) = AFND.eClosure(stateList)
        s = getState(stateClosure)
        AF.addState(s)

        if init:
            AF.initial = s
        if isAccepting:
            AF.addAccepting(s)

        for a in AFND.alphabet:
            if a == "&":
                continue
            trans = set()
            for toState in stateClosure:
                if a not in AFND.trans[toState]:
                    continue
                trans.update(AFND.trans[toState][a])
            if len(trans) == 0:
                continue
            (closure, isAccepting) = AFND.eClosure(list(trans))
            newState = getState(closure)
            if not newState in AF.trans and not newState in tState:
                tState.append(closure)
            AF.addTrans(s, a, newState)
    return AF

def format_er(ER):
    formatted_ER = []
    n_leafs = 1
    for i in range(len(ER) - 1):
        if ER[i].isalnum() and (ER[i + 1].isalnum() or ER[i + 1] == '('):
            formatted_ER.append(ER[i])
            formatted_ER.append('.')
        elif ER[i].isalnum() and ER[i + 1] == '#':
            formatted_ER.append(ER[i])
            formatted_ER.append('.')
        elif ER[i] == '*' and ER[i + 1] != '|':
            formatted_ER.append(ER[i])
            formatted_ER.append('.')
        else:
            formatted_ER.append(ER[i])
        if ER[i].isalnum():
            n_leafs += 1
    ER = ''.join(formatted_ER) + "#"
    return ER

def convertRPN(er):
    stack = []
    output = []
    operands = ["|", ".", "*", "?", "+"]
    precedencia = {".": 1, "|": 0}
    postfix = ["?", "*", "+"]
    prefix = ["|", "."]
    for symbol in er:
        if symbol in operands:
            if symbol in postfix:
                output.append(symbol)
            elif symbol in prefix:
                if len(stack) != 0:
                    if stack[-1] in precedencia.keys():
                        while precedencia[stack[-1]] >= precedencia[symbol]:
                                output.append(stack.pop())
                                if len(stack) == 0:
                                    break
                stack.append(symbol)
        elif symbol == "(":
            stack.append(symbol)
        elif symbol == ")":
            while stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        else:
            output.append(symbol)
    while len(stack) != 0:
        output.append(stack.pop())
    return output

def post_to_pre(ER):
    pre = []
    for symbol in ER[::-1]:
        pre.append(symbol)
    return pre

def construct_tree(ER):
    BINARY_OPS = [".", "|"]
    UNARY_OPS = ["*", "?", "+"]
    def parse(s):
        if s[0] in BINARY_OPS:
            lhs = parse(s[1:])
            lhs_end = 1 + len(lhs.span)
            rhs = parse(s[lhs_end:])
            rhs_end = lhs_end + len(rhs.span)
            return Node(s[:rhs_end], s[0], [rhs, lhs], 0, 0)
        elif s[0] in UNARY_OPS:
            operand = parse(s[1:])
            end = 1 + len(operand.span)
            return Node(s[:end], s[0], [operand], 0, 0)
        else:
            return Node(s[0], s[0], [], 0, 0)
    new_ER = parse("".join(ER))
    return new_ER

def isLeaf(s):
    if len(s.children) == 0:
        return True

def isNullable(s):
    if s.value == "&":
        return True
    elif s.value == "|":
        return isNullable(s.children[0]) or isNullable(s.children[1])
    elif s.value == "*":
        return True
    elif s.value == ".":
        return isNullable(s.children[0]) and isNullable(s.children[1])
    elif s.value == "?":
        return True
    else:
        return False

counter = 1
def parseLeaves(node):
    if isLeaf(node):
        global counter
        node.fPos = counter
        node.lPos = counter
        counter +=1
    else:
        for c in node.children:
            parseLeaves(c)

def first_and_lastPos(symbol):
    if symbol.fPos != 0 and symbol.lPos != 0:
        return [symbol.fPos, symbol.lPos]
    elif symbol.value == "*":
        symbol.fPos = first_and_lastPos(symbol.children[0])[0]
        symbol.lPos = symbol.fPos
        return [symbol.fPos, symbol.lPos]
    elif symbol.value == "|":
        symbol.fPos = [first_and_lastPos(symbol.children[0])[0]]
        symbol.fPos.append(first_and_lastPos(symbol.children[1])[0])
        symbol.lPos = symbol.fPos
        return [symbol.fPos, symbol.lPos]
    elif symbol.value == ".":
        if isNullable(symbol.children[0]):
            symbol.fPos = [first_and_lastPos(symbol.children[0])[0]]
            symbol.fPos.append(first_and_lastPos(symbol.children[1])[0])
        else:
            symbol.fPos = first_and_lastPos(symbol.children[0])[0]
        if isNullable(symbol.children[1]):
            symbol.lPos = [first_and_lastPos(symbol.children[0])[0]]
            symbol.lPos.append(first_and_lastPos(symbol.children[1])[0])
        else:
            symbol.lPos = first_and_lastPos(symbol.children[1])[0]
        return [symbol.fPos, symbol.lPos]

def flatten(it):
    for x in it:
        try:
            for y in flatten(x):
                yield y
        except TypeError:
            yield x

followp = {}
def follow(root):
    global followp
    followpos(root, followp)
    for c in root.children:
        if c.value == "#":
            followp[c.fPos] = []
            continue
        elif isLeaf(c):
            continue
        else:
            follow(c)
    return followp

def followpos(node, followp):
    if node.value == ".":
        c1 = node.children[0]
        c2 = node.children[1]
        first = list(flatten([c2.fPos]))
        last = list(flatten([c1.lPos]))
        for i in last:
            for pos in first:
                try:
                    followp[i].append(pos)
                except KeyError:
                    followp[i] = []
                    followp[i].append(pos)

    elif node.value == "*":
        l = list(flatten(node.lPos))
        first = list(flatten(node.fPos))
        for i in l:
            for pos in first:
                try:
                    followp[i].append(pos)
                except KeyError:
                    followp[i] = []
                    followp[i].append(pos)

    return followp

def getInputs(ER):
    r = set()
    operators = ['.', "*", "|", "?", "+"]
    for symbol in ER.span:
        if symbol not in operators:
            r.add(symbol)
    return r

correspond = {}
def getC(node, inputs, correspond):
    if node.value in inputs:
        try:
            correspond[node.value].append(node.fPos)
        except KeyError:
            correspond[node.value] = []
            correspond[node.value].append(node.fPos)

def getCorrespond(node, inputs):
    global correspond
    getC(node, inputs, correspond)
    for c in node.children:
        getCorrespond(c, inputs)
    return correspond

def createAFD(node, followp):
    AF = FiniteAutomata()
    state = "".join(str(e) for e in (list(flatten(node.fPos))))
    AF.initial = state
    Dstates = [state]
    inputs = getInputs(node)
    correspond = getCorrespond(node, inputs)

    while len(Dstates) != 0:
        S = Dstates.pop(0)
        S = "".join(str(e) for e in (S))
        AF.addState(S)
        for symbol in inputs:
            AF.alphabet.add(symbol)
            new = set()
            for c in correspond[symbol]:
                if str(c) in S:
                    for x in followp[c]:
                        new.add(x)
            new = "".join(str(e) for e in (new))
            if new not in AF.states:
                Dstates.append(new)
            AF.addTrans(S, symbol, new)
            for x in correspond["#"]:
                if str(x) in new:
                    AF.addAccepting(new)
    return AF

def ER_to_AFD(ER):
    ER = ER.regex['er'] + "#"
    regex = format_er(ER)
    rpn_regex = convertRPN(regex)
    prefixed = post_to_pre(rpn_regex)
    new = construct_tree(prefixed)
    parseLeaves(new)
    first_and_lastPos(new)
    followp = follow(new)
    AF = createAFD(new, followp)
    print("\n")
    print("Autômato:")
    AF.show()
    return AF
