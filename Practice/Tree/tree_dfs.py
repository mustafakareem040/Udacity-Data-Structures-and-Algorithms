class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


	
class Tree:
	def __init__(self, value, left=None, right=None):
		self.root = Node(value, left, right)


def dfs(start, goal=None, achieved = False):
	def _dfs(node, goal=None):
		nonlocal achieved
		arr = []
		if not node:
			return arr
		if goal and goal == node:
			achieved = True
			return arr
		if achieved:
			return arr
		arr.append(node)
		arr += _dfs(node.left, goal)
		arr += _dfs(node.right, goal)
		return arr
	return _dfs(start, goal)


x = Tree('A', Node('B', Node('C', Node('D', Node('E', Node('F', Node('G'), Node('H')))))))


print([i.value for i in dfs(x.root)]) # Whole Tree
print([i.value for i in dfs(x.root, x.root.left.left.left)]) # A B C


