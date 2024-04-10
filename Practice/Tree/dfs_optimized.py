class Node:
	def __init__(self, value):
		self.value = value
		self.children = []

	def add_child(self, node):
		self.children.append(node)

class Tree:
	def __init__(self, value):
		self.root = Node(value)

def dfs(node):
	arr = []
	if not node:
		return arr
	arr.append(node.value)
	for child in node.children:
		arr += dfs(child)

	return arr 

x = Tree(1)
x.root.add_child(Node(2))
x.root.add_child(Node(3))
x.root.children[0].add_child(Node(4))
x.root.children[1].add_child(Node(5))
x.root.children[0].children[0].add_child(Node(6))
x.root.add_child(Node(7))
print(dfs(x.root))