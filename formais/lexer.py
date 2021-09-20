import ply.lex as lex

def convert_ts_result(tokens):
    return [(token.value, token.type) for token in tokens]

def create_ts_result(filepath):
    with open(filepath) as f:
        source_code = f.read()

    tokens = []
    lexer = Lexer()
    lexer.build()
    lexer.input(source_code)
    while True:
        try:
            token = lexer.token()
        except ValueError as e:
            print(e)
            exit(1)

        if not token:
            break
        else:
            tokens.append(token)

    return convert_ts_result(tokens)


class Lexer:
    reserved_keywords = {
        'def': 'DEF',
        'if': 'IF',
        'for': 'FOR',
        'else': 'ELSE',
        'new': 'NEW',
        'int': 'INT_KEYWORD',
        'float': 'FLOAT_KEYWORD',
        'string': 'STRING_KEYWORD',
        'break': 'BREAK',
        'read': 'READ',
        'print': 'PRINT',
        'return': 'RETURN',
    }

    tokens = [
        # Reserved keywords
        *reserved_keywords.values(),

        # Brackets, parentesis and square brackets
        'LBRACKETS',
        'RBRACKETS',
        'LPAREN',
        'RPAREN',
        'LSQBRACKETS',
        'RSQBRACKETS',

        # Boolean operators
        'GREATER_THAN',
        'LOWER_THAN',
        'GREATER_OR_EQUALS_THAN',
        'LOWER_OR_EQUALS_THAN',
        'EQ_COMPARISON',
        'NEQ_COMPARISON',

        # Arithmetic operators
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'MODULE',

        # Delimiters
        'SEMICOLON',
        'COMMA',

        # Null
        'NULL',

        # Atribution
        'ATTRIBUTION',

        # Non-trivial tokens
        'IDENT',
        'FLOAT_CONSTANT',
        'INT_CONSTANT',
        'STRING_CONSTANT',
    ]

    t_LBRACKETS = r'{'
    t_RBRACKETS = r'}'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LSQBRACKETS = r'\['
    t_RSQBRACKETS = r'\]'

    t_GREATER_THAN = r'>'
    t_LOWER_THAN = r'<'
    t_GREATER_OR_EQUALS_THAN = r'>='
    t_LOWER_OR_EQUALS_THAN = r'<='
    t_EQ_COMPARISON = r'=='
    t_NEQ_COMPARISON = r'!='

    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'\/'
    t_MODULE = r'%'

    t_SEMICOLON = r';'
    t_COMMA = r','

    t_NULL = r'null'

    t_ATTRIBUTION = r'='

    t_STRING_CONSTANT = r'".*"'

    # Regular expressions with some actions

    def t_IDENT(self, t):
        r'[A-Za-z][A-Za-z0-9_]*'
        # Check identifier word is not a reserved keyword
        t.type = self.reserved_keywords.get(t.value, 'IDENT')
        return t

    def t_FLOAT_CONSTANT(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_INT_CONSTANT(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Define a rule so we can track line numbers

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

    # Error handling rule
    def find_column(self, token):
        line_start = self._input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1

    def t_error(self, t):
        raise ValueError(
            "Illegal character '%s' at line %s, column %s" %
            (t.value[0], t.lexer.lineno, self.find_column(t)))

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def input(self, source_code: str, **kwargs):
        self._input = source_code
        self.lexer.input(source_code, **kwargs)

    def token(self):
        return self.lexer.token()
