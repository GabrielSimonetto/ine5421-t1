import formais.automata as automata
import functools

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
def test_1_ends_in_aa_succeds():
    input = 'abaa'
    print(f"String computada: {input}")
    accepted = automata.compute(input)
    print(f"Resultado: {accepted}")
    assert accepted


@format_tests_nicely
def test_1_ends_in_aa_fails():
    print("Teste: test_1_ends_in_aa_fails")
    input = 'abba'
    print(f"String computada: {input}")
    accepted = automata.compute(input)
    print(f"Resultado: {accepted}")
    assert not accepted
