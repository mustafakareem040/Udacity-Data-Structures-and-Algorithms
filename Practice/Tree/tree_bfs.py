class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
		self.next = None

	def has_left_child(self):
		return self.left is not None

	def has_right_child(self):
		return self.right is not None


	
class Tree:
	def __init__(self, value):
		self.root = Node(value)


class Queue:
	def __init__(self, value = None):
		if value:
			self.front = Node(value)
		else:
			self.front = None
		self.tail = None

	def _enqueue(self, node):
		if not self.front:
			self.front = node
			return
		if not self.tail:
			self.tail = node
			self.front.next = self.tail
			return
		self.tail.next = node
		self.tail = self.tail.next

	def enqueue(self, value):
		node = Node(value)
		self._enqueue(node)

	def dequeue(self):
		value = self.front
		self.front = self.front.next
		return value

	def is_empty(self):
		return self.front == None

	def __bool__(self):
		return not self.is_empty()

	def __iadd__(self, queue):
		while queue:
			self._enqueue(queue.dequeue())


def breadth_first_search(node: Node):
	q = Queue()
	def process(node):
		print(node.value)
		if node.left:
			q._enqueue(node.left)
		if node.right:
			q._enqueue(node.right)
		if q:
			process(q.dequeue())
	process(node)


if __name__ == '__main__':
	x = Tree('A')
	x.root.left = Node('B')
	x.root.right = Node('C')
	x.root.left.right = Node('D')
	x.root.right.left = Node('E')
	breadth_first_search(x.root)