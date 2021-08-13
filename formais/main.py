from regular_expressions import RegularExpression
from conversions import ER_to_AFD

from formais import EXAMPLES_PATH

input = 'er: (a|b)*abb'
print(f"String computada: {input}")
ER = RegularExpression()
input_file = "2_er_to_afnd_1.txt"
ER.load(EXAMPLES_PATH / input_file) # --> ver se consigo passar na frente
                            # > mas nao agora -.-'
# TODO: rename this function
#       normalize everything to english
AFD = ER_to_AFD(ER)

recipe = AFD.return_constructor_recipe()

# ta esse plano de testar equivalencias de automatos nao vai funcionar de jeito nenhum.
#   voce precisaria definir equivalencia de conteudo, nao equivalencia de conteudo.
#   deve ter um jeito simples de descobrir como fazer isso, mas eu nao tenho tempo.
#   entao eu talvez precise de uma nova metodologia...
#   ou... eu posso esquecer a equivalencia de automato.
#   e focar em testes de aceitar ordenação de estados... ?
#   esse teste eh bem minoritário e bosta
#   acho que ano da pra fugir de realmente mostrar os estados
#   i don't like it, i don't like it one bit.

# ta, define uma condição de vitoria
#   define como isso deveria ser mostrado e comprovado que funciona eu acho.
#   eu gosto de testes... entao talvez mesmo testes ruins deveriam ser o correto?
#   ainda impressiona, I guess.
#  
#   mas eu tambem vou precisar de uma maneira de mostrar esse negocio.
#   eu posso ver como mostrar estilo guguinha eu acho?
#   eh, ve como os 2 grupos escolheram suas condições de vitoria, isso deve ser maneiro.
#   i mean, eu poderia... usar o formato do guguinha com os algoritmos da paloma.
#   that sounds pretty ok.
#
#   mano como eu queria que fosse simples testar isso.
#   CARA, OU, eu posso sempre ordenar as receitas.
#   nao isso tbm nao resolve eu acho, porque os nomes podem nao ser deterministicos
#   PROVAVELMENTE funciona, mas eu nao poderia inserir minhas ficha nisso com força.


# ^ nao criou uma AFD, na verdade.
#   a gente até pode... nao ligar pra isso?
#   se a gente soh mostrar sim, mas ai seria um HUGE tell
#   e nao permitiria testes.
#   ta, vamos ver o que eles estao imprimindo e se eh facil fazer uma conversao
#   deve ser... se AFD tem um init normal

# o que define uma AFD
# def __init__(self, trans=None, initial="0", accepting=None, states=None, alphabet=None):
#     self.trans = {} # Dicionário de Transições
#     self.initial = initial
#     self.accepting = set()
#     self.states = set() # Conjunto de estados
#     self.alphabet = set() # Conjunto de símobolos do alfabeto
