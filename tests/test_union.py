import functools

from formais.finite_automata import FiniteAutomata, NDFiniteAutomata

from formais import EXAMPLES_PATH

def format_tests_nicely(func):
    @functools.wraps(func)
    def wrapper_format_tests_nicely(*args, **kwargs):
        print()
        print("#### Novo Teste! #####")
        result = func(*args, **kwargs)
        print("#### Fim do Teste! #####")
        print()
        return result
    return wrapper_format_tests_nicely


@format_tests_nicely
def test_union():
    file_1 = '1_ends_in_aa.txt'
    file_2 = '4_odd_b.txt'
    expected_result_file = '1_union_4_result.txt'

    automata_1 = FiniteAutomata()
    automata_2 = FiniteAutomata()
    automata_1.load(EXAMPLES_PATH / file_1)
    automata_2.load(EXAMPLES_PATH / file_2)

    expected_result = NDFiniteAutomata()
    expected_result.load(EXAMPLES_PATH / expected_result_file)

    result = automata_1.union(automata_2)

    print('\nAutômato 1:\n')
    automata_1.show()
    print('\nAutômato 2:\n')
    automata_2.show()
    print('\nEXPECTED RESULT:\n')
    expected_result.show()
    print('\nUnião entre 1 e 2:\n')
    result.show()

    accepted = result == expected_result
    print(f'\nO resultado foi igual ao gabarito que possuimos? R: {accepted}')
    assert accepted