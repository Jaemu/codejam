def getBuildList(graph, nodes):
	buildList = []
	while(len(buildList) <= len(nodes)):
		seenNodes = []
		for node in graph.keys():
			children = graph[node]
			seenNodes = seenNodes + children
		if(len(seenNodes) is 0):
			buildList = buildList + graph.keys()
			break;
		nextToBuild = [x for x in graph.keys() if not x in seenNodes]
		if(len(nextToBuild) == 0):
			return 'No valid build - cycle detected'
		for node in nextToBuild:
			graph.pop(node)
		buildList = buildList + nextToBuild
	return buildList

def main():
	deps = [('a','c'), ('c', 'd'), ('c', 'b'), ('c', 'f')]
	#List of all individual nodes (keys) in the grap
	nodes = []
	graph = {}
	for i in xrange(len(deps)):
		val = deps[i][0]
		child = deps[i][1]
		node = None
		if not (val in nodes):
			nodes.append(val)
			graph[val] = []
		if not (child in nodes):
			nodes.append(child)
			graph[child] = []
		graph[val].append(child)
	print(getBuildList(graph, nodes))


if __name__ == '__main__':
	main()