class Node:
	data = None
	left = None
	right = None

	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def isBST(node):
	if node is None:
		return True
	elif node.left is None and node.right is None:
		return True
	else:
		if node.left is not None and node.left.data >= node.data:
			return False
		if node.right is not None and node.right.data <= node.data:
			return False
		else:
			return isBST(node.left) and isBST(node.right)



