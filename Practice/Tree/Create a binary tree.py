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
		self.levels = 1

	def print(self):
		node = self.root
		size = 2**self.levels
		print(str(node.value).center((12)))
		print("/", "\\".center(18))
		print(node.left.value, node.right.value.center(6))





