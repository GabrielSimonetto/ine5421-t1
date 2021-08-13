from textwrap import indent


class RegularExpression:

	# Inicializador
	def __init__(self):
		self.regex = {}

	# Pretty print
	def show(self):
		formatted = []
		for left, right in self.regex.items():
			formatted.append(f"{left}:{right}\n")
		print("".join(formatted))

	# Lê o arquivo
	def load(self, file):
		# Preenche a variável rules
		with open(file, 'r') as f:
			lines = [line.rstrip() for line in f]
			for line in lines:
				line = line.split(':')
				left = line[0]
				right = line[1][1:]
				self.regex[left] = right

	# Salva a GR em um arquivo local
	def save(self, filename):
		formatted = []
		with open(filename, "w") as writer:
			for left, right in self.regex.items():
				formatted.append(f'{left}:{right}\n')
			writer.write("".join(formatted))

    # # TODO: Rename to RE
    # # TODO: try to put this stuff into regular_expressions.py
    # def ER_to_AFD(self):
    #     ER = ER.regex['er'] + "#"
    #     regex = format_er(ER)
    #     rpn_regex = convertRPN(regex)
    #     prefixed = post_to_pre(rpn_regex)
    #     new = construct_tree(prefixed)
    #     parseLeaves(new)
    #     first_and_lastPos(new)
    #     print("Arvore Sintática:")
    #     print(new.__repr__())
    #     def show(symbol):
    #         print(symbol.value, "First Pos:", symbol.fPos, "Last Pos:", symbol.lPos)
    #         for c in symbol.children:
    #             show(c)
    #     print("First e Last Pos:")
    #     show(new)
    #     followp = follow(new)
    #     table = PrettyTable()
    #     table.add_column("n", list(followp.keys()))
    #     table.add_column("followpos", list(followp.values()))
    #     print("\n")
    #     print("Followpos:")
    #     print(table)
    #     AF = createAFD(new, followp)
    #     print("\n")
    #     print("Autômato:")
    #     AF.show()


class Node():
	def __init__(self, span, value, children, fPos, lPos):
		self.fPos = fPos
		self.lPos = lPos
		self.span = span
		self.value = value
		self.children = children

	def __repr__(self):
		out = self.value + '\n'
		out += indent('\n'.join(repr(c) for c in self.children), ' ' * 4)
		return out

