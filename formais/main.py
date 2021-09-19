from formais import EXAMPLES_PATH

from formais.cfg_processor import CfgProcessor, cfg_proc_reader


# def cfg_proc_reader(ll1_example_file):
#     cfg_proc = CfgProcessor()
#     cfg_proc.read(ll1_example_file)

#     return cfg_proc


filepath = EXAMPLES_PATH / '6_is_ll1_example.txt'
cfg_proc_ll1 = cfg_proc_reader(filepath)
print(cfg_proc_ll1.is_ll1())
assert(cfg_proc_ll1.is_ll1())

print()
print("Separate stuff")
print()

filepath = EXAMPLES_PATH / '6_not_ll1_example.txt'
cfg_proc_ll1 = cfg_proc_reader(filepath)
print(cfg_proc_ll1.is_ll1())
assert(not cfg_proc_ll1.is_ll1())





# from formais import EXAMPLES_PATH
# from formais.lexer import CC20202Lexer
# from formais import EXAMPLES_PATH

# filepath = EXAMPLES_PATH / 'ERASEME_lexer_input.txt'

# with open(filepath) as f:
#     source_code = f.read()

# tokens = []
# lexer = CC20202Lexer()
# # ok a gente builda com base na classe de antes
# # supostamente overcharging operadores
# lexer.build()
# # input pega o source code, supostamente a gente ja
# #   lida bem com o que entrar por causa da definição de linguagem
# #   que a gente ja tem na classe
# lexer.input(source_code)
# while True:
#     try:
#         # o lexer só serve pra ver se o token é valido ou nem.
#         token = lexer.token()
#     except ValueError as e:
#         print(e)
#         exit(1)

#     if not token:
#         break
#     else:
#         tokens.append(token)

# def create_ts_result(tokens):
#     """tokens: list[ply.lex.LexToken]
    
#     Returns: List of (Lexeme_Value, Token_Type) Tuples.
#     """

#     return [(token.value, token.type) for token in tokens]

# ts_result = create_ts_result(tokens)


