class Node:
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right

	def has_left_child(self):
		return self.left is not None

	def has_right_child(self):
		return self.right is not None


	
class Tree:
	def __init__(self, value):
		self.root = Node(value)


def search(node, target):
	if not node:
		return None
	if node.value == target:
		return node
	l = search(node.left, target)
	return l if l else search(node.right, target)


def pre_order(node):
	arr = []
	if not node:
		return arr
	arr.append(node)
	arr += pre_order(node.left)
	arr += pre_order(node.right)
	return arr

def in_order(node):
	arr = []
	if not node:
		return arr
	arr += in_order(node.left)
	arr.append(node)
	arr += in_order(node.right)
	return arr 

def post_order(node):
	arr = []
	if not node:
		return arr
	arr += in_order(node.left)
	arr += in_order(node.right)
	arr.append(node)
	return arr

x = Tree('apple')
x.root.left = Node('banana')
x.root.left.left = Node('date')
x.root.right = Node('cherry')

print(search(x.root, 'date'))
print([i.value for i in post_order(x.root)])


