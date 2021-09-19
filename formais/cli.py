import finite_automata
import regular_expressions
import conversions

class CLI:
    def __init__(self):
        pass

    def help(self):
        print('\n### Comandos: ###\n',
              'union - União entre AFD\n',
              'intersection - Interseção entre AFD\n',
              'determinization - Determinização de AFND\n',
              'minimization - Minimização de AFD\n',
              'er_to_afd - Conversão de ER para AFD\n',
              'help - Ajuda (este menu)'
        )

    def start(self):
        path = './examples/'

        while(True):
            self.help()
            command = input('Insira um comando: ')

            if command == 'union':
                input_file_1 = 'Arquivo contendo o primeiro AFD: '
                input_file_2 = 'Arquivo contendo o segundo AFD: '
                output_file = 'Nomeie o arquivo de saída: '

                AFD_1 = FiniteAutomata()
				AFD_1.load(path + input_file_1)
				AFD_2 = FiniteAutomata()
				AFD_2.load(path + input_file_2)
				AFD_union = AFD_1.union(AFD_2)
				AFD_union.save(output_file)

                print('\nAutômato 1:\n')
                AFD_1.show()
                print('\nAutômato 2:\n')
                AFD_2.show()
                print('\nUnião:\n')
                AFD_union.show()


            elif command == 'intersection':
                input_file_1 = 'Arquivo contendo o primeiro AFD: '
                input_file_2 = 'Arquivo contendo o segundo AFD: '
                output_file = 'Nomeie o arquivo de saída: '

                AFD_1 = FiniteAutomata()
				AFD_1.load(path + input_file_1)
				AFD_2 = FiniteAutomata()
				AFD_2.load(path + input_file_2)
				AFD_intersection = AFD_1.intersection(AFD_2)
				AFD_intersection.save(output_file)

                print('\nAFD 1:\n')
                AFD_1.show()
                print('\nAFD 2:\n')
                AFD_2.show()
                print('\nInterseção:\n')
                AFD_union.show()

            elif command == 'determinization':
                input_file = 'Arquivo contendo um AFND: '
                output_file = 'Nomeie o arquivo de saída: '

                AFND = NDFiniteAutomata()
                AFND.load(path + input_file)
                AFD = determinize(AFND)

                print('\nAF não determinístico:\n')
                AFND.show()
                print('\nAF determinizado:\n')
                AFD.show()

            elif command == 'minimization':
                input_file == 'Arquivo contendo um AFD: '
                output_file == 'Nomeie o arquivo de saída: '

                AFD = FiniteAutomata()
                AFD.load(path + input_file)
                AFD_minimized = minimize(AFD)
                AFD_minimized.save(output_file)

                print('\nAFD inicial:\n')
                AFND.show()
                print('\nAFD minimizado:\n')
                AFD_minimized.show()

            elif command == 'er_to_afd':
                input_file == 'Arquivo contendo uma ER: '
                output_file == 'Nomeie o arquivo de saída: '

                ER = RegularExpression()
                ER.load(path + input_file)
                AFD = ER_to_AFD(ER)
                AFD.save(output_file)

                print('\nExpressão regular:\n')
                ER.show()
                print('\nAFD equivalente:\n')
                AFD.show()

            elif command == 'help':
                self.help()
            else:
                print('Comando inexistente.')
