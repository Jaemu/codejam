class Node:
	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def printDFS(root):
	if(root is None):
		return []
	if(root.left is None and root.right is None):
		return [root.val]
	if(root.left is None):
		return [root.val] + printDFS(root.right)
	if(root.right is None):
		return [root.val] + printDFS(root.left)
	return [root.val] + printDFS(root.left) + printDFS(root.right)


def printBFS(root):
	if(root is None):
		return []
	visited = [root.val]
	children = []
	if(root.left is None and root.right is None):
		return visited
	if(root.left is None):
		children.append(root.right)
	if(root.right is None):
		children.append(root.left)
	children.append(root.left)
	children.append(root.right)
	while(len(children) > 0):
		root = children.pop(0)
		visited.append(root.val)
		if(root.left is None and root.right is None):
			continue
		if(root.left is None):
			children.append(root.right)
			continue
		if(root.right is None):
			children.append(root.left)
			continue
		children.append(root.left)
		children.append(root.right)
	return visited




	
def main():
	tree = Node(5)
	tree.left = Node(6)
	tree.right = Node(8)
	tree.left.left = Node(11)
	tree.right.left = Node(9)
	tree.right.right = Node(10)

	print(printDFS(tree))
	print(printBFS(tree))


if __name__ == '__main__':
	main()