import functools

from formais.lexer import create_ts_result

from formais import EXAMPLES_PATH

expected_ERASEME_lexer_input_result = [
    ("{", "LBRACKETS"),
    ("{", "LBRACKETS"),
    ("float", "FLOAT_KEYWORD"),
    ("x", "IDENT"),
    (";", "SEMICOLON"),
    ("float", "FLOAT_KEYWORD"),
    ("z", "IDENT"),
    (";", "SEMICOLON"),
    ("int", "INT_KEYWORD"),
    ("i", "IDENT"),
    (";", "SEMICOLON"),
    ("int", "INT_KEYWORD"),
    ("max", "IDENT"),
    (";", "SEMICOLON"),
    ("x", "IDENT"),
    ("=", "ATTRIBUTION"),
    (0, "INT_CONSTANT"),
    (";", "SEMICOLON"),
    ("max", "IDENT"),
    ("=", "ATTRIBUTION"),
    (10000, "INT_CONSTANT"),
    (";", "SEMICOLON"),
    ("for", "FOR"),
    ("(", "LPAREN"),
    ("i", "IDENT"),
    ("=", "ATTRIBUTION"),
    (1, "INT_CONSTANT"),
    (";", "SEMICOLON"),
    ("i", "IDENT"),
    ("<=", "LOWER_OR_EQUALS_THAN"),
    ("max", "IDENT"),
    (";", "SEMICOLON"),
    ("i", "IDENT"),
    ("=", "ATTRIBUTION"),
    ("i", "IDENT"),
    ("+", "PLUS"),
    (1, "INT_CONSTANT"),
    (")", "RPAREN"),
    ("{", "LBRACKETS"),
    ("print", "PRINT"),
    ("x", "IDENT"),
    (";", "SEMICOLON"),
    ("x", "IDENT"),
    ("=", "ATTRIBUTION"),
    ("x", "IDENT"),
    ("+", "PLUS"),
    (0.001, "FLOAT_CONSTANT"),
    (";", "SEMICOLON"),
    ("z", "IDENT"),
    ("=", "ATTRIBUTION"),
    ("x", "IDENT"),
    (";", "SEMICOLON"),
    ("if", "IF"),
    ("(", "LPAREN"),
    ("z", "IDENT"),
    ("!=", "NEQ_COMPARISON"),
    ("x", "IDENT"),
    (")", "RPAREN"),
    ("{", "LBRACKETS"),
    ("print", "PRINT"),
    (
        '"Erro numérico na atribuição de números na notação ponto flutuante!"',
        "STRING_CONSTANT",
    ),
    (";", "SEMICOLON"),
    ("break", "BREAK"),
    (";", "SEMICOLON"),
    ("}", "RBRACKETS"),
    ("}", "RBRACKETS"),
    ("}", "RBRACKETS"),
    ("{", "LBRACKETS"),
    ("int", "INT_KEYWORD"),
    ("y", "IDENT"),
    (";", "SEMICOLON"),
    ("int", "INT_KEYWORD"),
    ("j", "IDENT"),
    (";", "SEMICOLON"),
    ("int", "INT_KEYWORD"),
    ("i", "IDENT"),
    (";", "SEMICOLON"),
    ("y", "IDENT"),
    ("=", "ATTRIBUTION"),
    ("new", "NEW"),
    ("int", "INT_KEYWORD"),
    ("[", "LSQBRACKETS"),
    (10, "INT_CONSTANT"),
    ("]", "RSQBRACKETS"),
    (";", "SEMICOLON"),
    ("j", "IDENT"),
    ("=", "ATTRIBUTION"),
    (0, "INT_CONSTANT"),
    (";", "SEMICOLON"),
    ("for", "FOR"),
    ("(", "LPAREN"),
    ("i", "IDENT"),
    ("=", "ATTRIBUTION"),
    (0, "INT_CONSTANT"),
    (";", "SEMICOLON"),
    ("i", "IDENT"),
    ("<", "LOWER_THAN"),
    (20, "INT_CONSTANT"),
    (";", "SEMICOLON"),
    ("i", "IDENT"),
    ("=", "ATTRIBUTION"),
    ("i", "IDENT"),
    ("+", "PLUS"),
    (1, "INT_CONSTANT"),
    (")", "RPAREN"),
    ("{", "LBRACKETS"),
    ("if", "IF"),
    ("(", "LPAREN"),
    ("i", "IDENT"),
    ("%", "MODULE"),
    (2, "INT_CONSTANT"),
    ("==", "EQ_COMPARISON"),
    (0, "INT_CONSTANT"),
    (")", "RPAREN"),
    ("{", "LBRACKETS"),
    ("y", "IDENT"),
    ("[", "LSQBRACKETS"),
    ("j", "IDENT"),
    ("]", "RSQBRACKETS"),
    ("=", "ATTRIBUTION"),
    ("i", "IDENT"),
    ("+", "PLUS"),
    (1, "INT_CONSTANT"),
    (";", "SEMICOLON"),
    ("j", "IDENT"),
    ("=", "ATTRIBUTION"),
    ("j", "IDENT"),
    ("+", "PLUS"),
    (1, "INT_CONSTANT"),
    (";", "SEMICOLON"),
    ("}", "RBRACKETS"),
    ("else", "ELSE"),
    ("{", "LBRACKETS"),
    ("print", "PRINT"),
    (0, "INT_CONSTANT"),
    (";", "SEMICOLON"),
    ("}", "RBRACKETS"),
    ("}", "RBRACKETS"),
    ("for", "FOR"),
    ("(", "LPAREN"),
    ("i", "IDENT"),
    ("=", "ATTRIBUTION"),
    (0, "INT_CONSTANT"),
    (";", "SEMICOLON"),
    ("i", "IDENT"),
    ("<", "LOWER_THAN"),
    (10, "INT_CONSTANT"),
    (";", "SEMICOLON"),
    ("i", "IDENT"),
    ("=", "ATTRIBUTION"),
    ("i", "IDENT"),
    ("+", "PLUS"),
    (1, "INT_CONSTANT"),
    (")", "RPAREN"),
    ("{", "LBRACKETS"),
    ("print", "PRINT"),
    ("y", "IDENT"),
    ("[", "LSQBRACKETS"),
    ("i", "IDENT"),
    ("]", "RSQBRACKETS"),
    (";", "SEMICOLON"),
    ("}", "RBRACKETS"),
    ("return", "RETURN"),
    (";", "SEMICOLON"),
    ("}", "RBRACKETS"),
    ("}", "RBRACKETS"),
]


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
def test_ERASEME_lexer_input_test():
    filepath = EXAMPLES_PATH / "ERASEME_lexer_input.txt"
    result = create_ts_result(filepath)

    accepted = result == expected_ERASEME_lexer_input_result
    print(f"\nO resultado foi igual ao gabarito que possuimos? R: {accepted}")
    assert accepted