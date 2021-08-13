from regular_expressions import RegularExpression
from conversions import ER_to_AFD, AFND_determinizer

from finite_automata import NDFiniteAutomata

from formais import EXAMPLES_PATH

input_file = '4_simple_determination_2.txt'
output_file = '4_simple_determination_2_result.txt'

AFND = NDFiniteAutomata()
AFND.load(EXAMPLES_PATH / input_file)
AFD = AFND_determinizer(AFND)
AFD.save(EXAMPLES_PATH / output_file)

print('\nSeu AFND de entrada foi:\n')
AFND.show()
print('\nSeu AFD de saída é:\n')
AFD.show()
