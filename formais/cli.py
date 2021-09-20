#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit

from finite_automata import FiniteAutomata, NDFiniteAutomata
from conversions import determinize, minimize, ER_to_AFD
from regular_expressions import RegularExpression
from cfg_processor import *
from cfg_parser import *
from lexer import create_ts_result

from __init__ import EXAMPLES_PATH, OUTPUT_PATH

class CLI:
    def __init__(self):
        pass

    def help(self):
        print('\n### Comandos: ###\n',
              'union           - União entre AFD\n',
              'intersection    - Interseção entre AFD\n',
              'determinization - Determinização de AFND\n',
              'minimization    - Minimização de AFD\n',
              'er_to_afd       - Conversão de ER para AFD\n',
              'recognition     - Verifica se um AF reconhece certa palavra\n',
              'analysis_table  - Mostra a tabela de análise de uma gramática LL(1)\n',
              'symbol_table    - Mostra a tabela de símbolos de uma linguagem\n',
              'help            - Ajuda (mostra este menu)\n',
              'exit            - Sai do programa'
        )

    def exit(self):
        print('\nAté mais!')
        exit(0)

    def start(self):
        self.help()

        while(True):
            command = input('\nInsira um comando: ')

            if command == 'union':
                default_file_1 = '1_ends_in_aa.txt'
                default_file_2 = '4_odd_b.txt'
                default_output_file = 'testing_cli_union.txt'

                aux_input_file_1 = input(f'Arquivo contendo o primeiro AFD: (default: {default_file_1})')
                aux_input_file_2 = input(f'Arquivo contendo o segundo AFD: (default: {default_file_2})')
                aux_output_file = input(f'Nomeie o arquivo de saída: (default: {default_output_file})')

                input_file_1 = default_file_1 if aux_input_file_1 == '' else aux_input_file_1
                input_file_2 = default_file_2 if aux_input_file_2 == '' else aux_input_file_2
                output_file =  default_output_file if aux_output_file  == '' else aux_output_file

                AFD_1 = FiniteAutomata()
                AFD_1.load(EXAMPLES_PATH / input_file_1)
                AFD_2 = FiniteAutomata()
                AFD_2.load(EXAMPLES_PATH / input_file_2)
                AFD_union = AFD_1.union(AFD_2)
                AFD_union.save(OUTPUT_PATH / output_file)

                print('\nAutômato 1:\n')
                AFD_1.show()
                print('\nAutômato 2:\n')
                AFD_2.show()
                print('\nUnião:\n')
                AFD_union.show()


            elif command == 'intersection':
                default_file_1 = '1_ends_in_aa.txt'
                default_file_2 = '4_odd_b.txt'
                default_output_file = 'testing_cli_intersection.txt'

                aux_input_file_1 = input(f'Arquivo contendo o primeiro AFD: (default: {default_file_1})')
                aux_input_file_2 = input(f'Arquivo contendo o segundo AFD: (default: {default_file_2})')
                aux_output_file = input(f'Nomeie o arquivo de saída: (default {default_output_file})')

                input_file_1 = default_file_1 if aux_input_file_1 == '' else aux_input_file_1
                input_file_2 = default_file_2 if aux_input_file_2 == '' else aux_input_file_2
                output_file =  default_output_file if aux_output_file  == '' else aux_output_file

                AFD_1 = FiniteAutomata()
                AFD_1.load(EXAMPLES_PATH / input_file_1)
                AFD_2 = FiniteAutomata()
                AFD_2.load(EXAMPLES_PATH / input_file_2)
                AFD_intersection = AFD_1.intersection(AFD_2)
                AFD_intersection.save(OUTPUT_PATH / output_file)

                print('\nAFD 1:\n')
                AFD_1.show()
                print('\nAFD 2:\n')
                AFD_2.show()
                print('\nInterseção:\n')
                AFD_intersection.show()

            elif command == 'determinization':
                default_input_file = '4_simple_determination_2.txt'
                default_output_file = 'testing_cli_determinization.txt'

                aux_input_file_1 = input(f'Arquivo contendo um AFND: (default: {default_input_file})')
                aux_output_file = input(f'Nomeie o arquivo de saída: (default {default_output_file})')

                input_file = default_input_file if aux_input_file_1 == '' else aux_input_file_1
                output_file =  default_output_file if aux_output_file  == '' else aux_output_file

                AFND = NDFiniteAutomata()
                AFND.load(EXAMPLES_PATH / input_file)
                AFD = determinize(AFND)
                AFD.save(OUTPUT_PATH / output_file)

                print('\nAF não determinístico:\n')
                AFND.show()
                print('\nAF determinizado:\n')
                AFD.show()

            elif command == 'minimization':
                default_input_file = '1_ends_in_aa.txt'
                default_output_file = 'testing_cli_minimization.txt'

                aux_input_file = input(f'Arquivo contendo um AFD: (default: {default_input_file})')
                aux_output_file = input(f'Nomeie o arquivo de saída: (default {default_output_file})')

                input_file = default_input_file if aux_input_file == '' else aux_input_file
                output_file =  default_output_file if aux_output_file  == '' else aux_output_file

                AFD = FiniteAutomata()
                AFD.load(EXAMPLES_PATH / input_file)
                AFD_minimized = minimize(AFD)
                AFD_minimized.save(OUTPUT_PATH / output_file)

                print('\nAFD inicial:\n')
                AFND.show()
                print('\nAFD minimizado:\n')
                AFD_minimized.show()

            elif command == 'er_to_afd':
                default_input_file = '2_er_to_afd_1.txt'
                default_output_file = 'testing_cli_er_to_afd.txt'

                aux_input_file = input(f'Arquivo contendo uma ER: (default: {default_input_file})')
                aux_output_file = input(f'Nomeie o arquivo de saída: (default {default_output_file})')

                input_file = default_input_file if aux_input_file == '' else aux_input_file
                output_file =  default_output_file if aux_output_file  == '' else aux_output_file

                ER = RegularExpression()
                ER.load(EXAMPLES_PATH / input_file)
                AFD = ER_to_AFD(ER)
                AFD.save(OUTPUT_PATH / output_file)

                print('\nExpressão regular:\n')
                ER.show()
                print('\nAFD equivalente:\n')
                AFD.show()

            elif command == 'recognition':
                default_input_file = '1_ends_in_aa.txt'
                aux_input_file = input(f'Arquivo contendo um AF: (default: {default_input_file})')
                input_file = default_input_file if aux_input_file == '' else aux_input_file

                word = input('Palavra a ser reconhecida: ')

                AF = FiniteAutomata()
                AF.load(EXAMPLES_PATH / input_file)
                recognizes = AF.recognizes(word)

                print('\nAutômato:\n')
                AF.show()
                if recognizes:
                    print('\nO autômato reconhece a palavra ' + word + '.')
                else:
                    print('\nO autômato não reconhece a palavra ' + word + '.')

            elif command == 'analysis_table':
                default_input_file = '6_not_ll1_example.txt' # TODO: Fix matrix printing then set default file as 6_is_ll1_example.txt
                aux_input_file = input(f'Arquivo contendo uma GLC: (default: {default_input_file})')
                input_file = default_input_file if aux_input_file == '' else aux_input_file

                cfg = cfg_proc_reader(EXAMPLES_PATH / input_file)
                if cfg.is_ll1():
                    print('\nTabela de análise gerada:\n')
                    print(cfg.generate_matrix())
                else:
                    print('\nNão foi possível gerar a tabela, pois a gramática não é LL(1)')

            elif command == 'symbol_table':
                default_input_file = 'simple_lexer_input.txt'
                aux_input_file = input(f'Arquivo contendo o código fonte a ser analisado: (default: {default_input_file})\n')
                input_file = default_input_file if aux_input_file == '' else aux_input_file

                input_text = open(EXAMPLES_PATH / input_file)
                for line in input_text:
                    print(line)
                symbol_table = create_ts_result(EXAMPLES_PATH / input_file)
                for value, type in symbol_table:
                    print(f'{value}: {type}')

            elif command == 'help':
                self.help()

            elif command == 'exit':
                self.exit()

            else:
                print('Comando inexistente. Para ver os comandos disponíveis, digite help.')
