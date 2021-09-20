import functools

from formais.cfg_processor import cfg_proc_reader
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
def test_asserts_a_LL1_cfg_is_LL1():
    filepath = EXAMPLES_PATH / '6_is_ll1_example.txt'
    cfg = cfg_proc_reader(filepath)

    is_ll1 = cfg.is_ll1()
    print(f"\nEssa CFG que é LL1 é identificada como LL1? R: {is_ll1}")
    assert is_ll1


@format_tests_nicely
def test_asserts_a_LL1_cfg_is_LL1():
    filepath = EXAMPLES_PATH / '6_not_ll1_example.txt'
    cfg = cfg_proc_reader(filepath)

    is_ll1 = cfg.is_ll1()
    print(f"\nEssa CFG que não é LL1 é identificada como LL1? R: {is_ll1}")
    assert not is_ll1


@format_tests_nicely
def test_asserts_simple_lexer_is_LL1():
    filepath = EXAMPLES_PATH / '7_describing_simple_lexer_as_cfg.txt'
    cfg = cfg_proc_reader(filepath)

    is_ll1 = cfg.is_ll1()
    print(f"\nEssa CFG que é LL1 é identificada como LL1? R: {is_ll1}")
    assert is_ll1
