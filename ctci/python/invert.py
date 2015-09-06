class TreeNode():
	val = None
	left = None
	right = None

	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def binTree():
	root = TreeNode(4)
	root.left = TreeNode(2)
	root.right = TreeNode(7)
	root.left.left = TreeNode(1)
	root.left.right = TreeNode(3)
	root.right.left = TreeNode(6)
	root.right.right = TreeNode(9)

	return root

def invertTree(node):
	#No nodes to swap -- return the current node
	if node is None:
		return node
	if (node.left is None and node.right is None):
		return node
	else:
		if node.left is None:
			node.left = node.right
		elif node.right is None:
			node.right = node.left
		else:
			temp = node.left
			node.left = node.right
			node.right = temp
		node.left = invertTree(node.left)
		node.right = invertTree(node.right)
		return node

def printTree(node):
	if node.left is not None:
		printTree(node.left)
	if node is not None:
		print(node.val)
	if node.right is not None:
		printTree(node.right)

if __name__ == '__main__':
	t = binTree()
	v = invertTree(t)
	printTree(v)
