import functools

from formais.regular_expressions import RegularExpression
from formais.conversions import ER_to_AFD

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
def test_1_make_finite_automata_from_regex_and_recognize_language():
    input_regex = 'er: (a|b)*abb'
    print(f"Regex computado: {input_regex}")
    ER = RegularExpression()
    input_file = "2_er_to_afd_1.txt"
    ER.load(EXAMPLES_PATH / input_file)
    AFD = ER_to_AFD(ER)

    # Test a) - should accept 
    word_input = 'ababaaabb'   
    accepted  = AFD.recognizes(word_input)
    print(f"input a) na AFD gerada, deve ser aceito: {word_input}")
    print(f"Resultado: {accepted}")
    assert accepted

    # Test b) - should not accept 
    word_input = 'ab'   
    accepted  = AFD.recognizes(word_input)
    print(f"input b) na AFD gerada, não deve ser aceito: {word_input}")
    print(f"Resultado: {accepted}")
    assert not accepted
