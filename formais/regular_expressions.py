from textwrap import indent


class RegularExpression:

	def __init__(self):
		self.regex = {}

	def show(self):
		formatted = []
		for left, right in self.regex.items():
			formatted.append(f"{left}:{right}\n")
		print("".join(formatted))

	def load(self, file):
		with open(file, 'r') as f:
			lines = [line.rstrip() for line in f]
			for line in lines:
				line = line.split(':')
				left = line[0]
				right = line[1][1:]
				self.regex[left] = right

	def save(self, filename):
		formatted = []
		with open(filename, "w") as writer:
			for left, right in self.regex.items():
				formatted.append(f'{left}:{right}\n')
			writer.write("".join(formatted))


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
