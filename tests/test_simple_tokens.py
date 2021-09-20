import functools

from formais.lexer import create_ts_result

from formais import EXAMPLES_PATH

expected_simple_lexer_input_result = [('def', 'DEF'),
 ('myFunc', 'IDENT'),
 ('int', 'INT_KEYWORD'),
 ('i', 'IDENT'),
 (';', 'SEMICOLON'),
 ('i', 'IDENT'),
 ('=', 'ATTRIBUTION'),
 (4, 'INT_CONSTANT'),
 (';', 'SEMICOLON'),
 ('if', 'IF'),
 ('i', 'IDENT'),
 ('>', 'GREATER_THAN'),
 (0, 'INT_CONSTANT'),
 ('{', 'LBRACKETS'),
 ('print', 'PRINT'),
 ('"i eh positivo"', 'STRING_CONSTANT'),
 (';', 'SEMICOLON'),
 ('print', 'PRINT'),
 ('i', 'IDENT'),
 (';', 'SEMICOLON'),
 ('}', 'RBRACKETS')]

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
def test_simple_lexer_input_test():
    filepath = EXAMPLES_PATH / "simple_lexer_input.txt"
    result = create_ts_result(filepath)

    accepted = result == expected_simple_lexer_input_result
    print(f"\nO resultado foi igual ao gabarito que possuimos? R: {accepted}")
    assert accepted
