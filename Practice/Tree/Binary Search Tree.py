class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = None
		self.next = None
		self.right = None

	def has_right_child(self):
		return bool(self.left)

	def has_left_child(self):
		return bool(self.right)


	def set_left(self, node):
		self.left = node

	def set_right(self, node):
		self.right = node

class BinaryTree:
	def __init__(self):
		self.root = None
		
	def insert(self, value):
		# O(log n) insert
		if self.root is None:
			self.root = Node(value)
			return
		root = self.root
		while root:
			if value == root.value: 
				break
			if not root.left and not root.right:
				if value > root.value:
					root.right = Node(value)
				else:
					root.left = Node(value)
				break
			elif not root.left and root.right:
				if value < root.value:
					root.left = Node(value)
					break
				else:
					root = root.right
			elif not root.right and root.left:
				if value > root.value:
					root.right = Node(value)
					break
				else:
					root = root.left
			else:
				if value > root.value:
					root = root.right
				else:
					root = root.left
	def search(self, value):
		# O(log n) Search
		root = self.root
		if not root:
			return False
		while root:
			if value == root.value:
				return True
			if value > root.value:
				root = root.right
			else:
				root = root.left
		return False

	def delete(self, value):
		root = self.root
		if not root:
			return None
		if root.value == value:
			self.root = None
		link = None
		while root:
			if root.value == value:
				break
			link = root
			if value > root.value:
				root = root.right
			else:
				root = root.left
			if root is None:
				return
		if root.has_right_child() and root.has_left_child():
			child = root.right
			if not child.left:
				if link.left == root:
					link.left = child
				else:
					link.right = child
			else:
				p = None
				while child:
					p = child
					child = child.left
				p.left = None
				r = child.right
				child.left = root.left
				child.right = root.right
				if link.left == root:
					link.left = child
				else:
					link.right = child
				self._extend(r)

		elif root.has_right_child() or root.has_left_child():
			if link.left == root:
				link.left = root.right or root.left
			else:
				link.right = root.right or root.left
		else:
			if link.left == root:
				link.left = None
			else:
				link.right = None
		del root

	def _extend(self, node):
		pass





if __name__ == '__main__':
	x = BinaryTree()
	x.insert(5)
	x.insert(4)
	x.insert(4.5)
	x.insert(9)
	x.insert(2)
	x.insert(3)
	x.insert(10)
	x.insert(13)
	x.insert(20)
	x.insert(0)
	x.insert(7)
	x.insert(5)
	x.delete(4)
	print(x.search(4))