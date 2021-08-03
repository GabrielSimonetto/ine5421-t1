from formais.automata import Automata

# Q: a - A, B, C; b - C;
# def parse_automata(name, type_input):
#     f = open("./input/" + name + "." + type_input + ".txt", "r")
#     _automata = automata.Automata(name)

def parse_automata(name):
    f = open("./examples/" + name, "r")
    _automata = Automata(name)
    first = True
    initial = ""
    end_states = []

    for line in f:
        line = line.replace(" ", "")
        parts = line.split(':')
        state = parts[0]
        if state[0] == '*':
            end_states.append(state[1:])
            state = state[1:]
        
        transitions = parts[1].split(';')
        transition_list = []
        for transition in transitions:
            parts = transition.split('-')
            if len(parts) > 1:
                state_list = parts[1].split(',')
                transition_list.append((parts[0], state_list))
        
        if first:
            initial = state
            first = False
        _automata.add_state(state, transition_list)
    
    for state in end_states:
        _automata.set_end_state(state)
    
    _automata.set_start(initial)
    return _automata


automato = parse_automata("1_ends_in_aa.txt")