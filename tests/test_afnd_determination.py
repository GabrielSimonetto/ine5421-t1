import functools

from formais.conversions import AFND_determinizer
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
def test_determinize_3_simple_determination():
    input_file = '3_simple_determination.txt'
    expected_result_file = '3_simple_determination_result.txt'

    AFND = NDFiniteAutomata()
    AFND.load(EXAMPLES_PATH / input_file)

    expected_AFD = FiniteAutomata()
    expected_AFD.load(EXAMPLES_PATH / expected_result_file)

    result_AFD = AFND_determinizer(AFND)

    print('\nSeu AFND de entrada foi:\n')
    AFND.show()
    print('\nSeu AFD de saída é:\n')
    result_AFD.show()

    accepted = result_AFD == expected_AFD
    print(f'\nO resultado foi igual ao gabarito que possuimos? R: {accepted}')
    assert accepted


@format_tests_nicely
def test_determinize_4_simple_determination():
    input_file = '4_simple_determination_2.txt'
    expected_result_file = '4_simple_determination_2_result.txt'

    AFND = NDFiniteAutomata()
    AFND.load(EXAMPLES_PATH / input_file)

    expected_AFD = FiniteAutomata()
    expected_AFD.load(EXAMPLES_PATH / expected_result_file)

    result_AFD = AFND_determinizer(AFND)

    print('\nSeu AFND de entrada foi:\n')
    AFND.show()
    print('\nSeu AFD de saída é:\n')
    result_AFD.show()

    accepted = result_AFD == expected_AFD
    print(f'\nO resultado foi igual ao gabarito que possuimos? R: {accepted}')
    assert accepted
    