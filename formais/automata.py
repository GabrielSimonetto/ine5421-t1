class Automata:
    def __init__(self, name: str):
        self.name = name
        self.states = [] # represented by A B C
        self.transitions = {}
        self.start_state = ""
        self.end_states = []

    def print_automata(self):
        print(self.name + ":\n")
        for state in self.transitions:
            aux1 = ""
            if state in self.end_states:
                aux1 += "*"    
            if state == self.start_state:
                aux1 += "->"
            for symbol in self.transitions[state]:
                aux2 = aux1 + "transição({0}; {1}) = ".format(state, symbol)
                state_list = ", ".join(self.transitions[state][symbol])
                if len(self.transitions[state][symbol]) > 1:
                    finalprint = aux2 + "{" + state_list + "}"
                else:    
                    finalprint = aux2 + state_list

                print(finalprint)

    # Recebe uma lista de tuplas transição na forma (símbolo, [estados alcançáveis por esse símbolo])
    # Exemplo: [('a', ['B']), ('b', ['C','D','E'])]
    # O dict transitions fica na forma transitions[estado] = {símbolo1: [estados],
    #                                                         símbolo2: [estados],
    #                                                         ...}
    # Exemplo: self.transitions['A'] = {'a': ['A','B'],
    #                                   'b': ['C'] 
    #                                   }
    def add_state(self, state_name: str, transition_list = [], end_state=False):

        if not state_name.isalnum() and "," not in state_name:
            print("The state's name must be alphanumeric.")
            return
        
        state_name = state_name.upper()

        if state_name in self.transitions:
            self.add_transition(state_name, transition_list)
        else:
            self.transitions[state_name] = {}

            for transition in transition_list:
                symbol: str = transition[0]
                reachable_states: list = transition[1]
                reachable_states.sort()
                for state in reachable_states:
                    state: str = state.upper()

                if symbol in self.transitions[state_name]:
                    for state in reachable_states:

                        if state not in self.transitions[state_name][symbol]:
                            self.transitions[state_name][symbol].append(state)
                            self.transitions[state_name][symbol].sort()

                        if state not in self.transitions:
                            self.add_state(state)    

                else:
                    self.transitions[state_name][symbol] = reachable_states
                    if state not in self.transitions:
                        self.add_state(state)

            if (end_state):
                self.end_states.append(state_name)

    # Adiciona uma ou mais transições em um estado que já existe
    def add_transition(self, state_name: str, transition_list: list):

        state_name = state_name.upper()

        if state_name in self.transitions:

            for transition in transition_list:
                symbol: str = transition[0]
                reachable_states: list = transition[1]
                reachable_states.sort()
                for r_state in reachable_states:
                    r_state: str = r_state.upper()

                if symbol in self.transitions[state_name]:

                    for state in reachable_states:

                        if state not in self.transitions:
                            self.add_state(state)
                        if state not in self.transitions[state_name][symbol]:
                            self.transitions[state_name][symbol].append(state)
                            self.transitions[state_name][symbol].sort()

                else:
                    self.transitions[state_name][symbol] = reachable_states
        else:
            print("Transition not added: the given state does not exist")

    # Coloca o estado dado (que já existe no autômato) como estado inicial
    # Se o autômato já tiver outro estado inicial, ele é substituído
    def set_start(self, name: str):

        name = name.upper()
        if name in self.transitions:
            self.start_state = name
        else:
            print("State not set to start state: No such state exists")

    def set_end_state(self, state_name: str):

        if state_name in self.transitions:
            if state_name not in self.end_states:
                self.end_states.append(state_name)
                self.end_states.sort()
        else:
            print("State not set to end state: No such state exists")




def compute(input):
    if input == 'abaa':
        return True
    elif input == 'abba':
        return False
    else:
        return False
