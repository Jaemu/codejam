class Person:
	height = None
	weight = None

	def __init__(self, height=0, weight=0):
		self.height = height
		self.weight = weight

	def __hash__(self):
		return hash(repr(self))

	def __str__(self):
		return('(' + str(self.height) + ', ' + str(self.weight) + ')') 

def getRootCandidate(dag):
	for person in dag.keys():
		isCandidate = True
		for otherPerson in dag.keys():
			neighbors = dag[otherPerson]
			if person in neighbors:
				isCandidate = False
				break
		if isCandidate:
			return person
	return Person(-1,-1)


def getTower(people):
	result = []
	peopleDag = {}
	resultString = ''
	for i in xrange(len(people)):
		currentPerson = Person(people[i][0], people[i][1])
		if not currentPerson in peopleDag.keys():
			peopleDag[currentPerson] = []
		for person in peopleDag:
			if person.height < currentPerson.height and person.weight < currentPerson.weight:
				peopleDag[person].append(currentPerson)
	while len(result) < len(people):
		root = getRootCandidate(peopleDag)
		if(root.height is -1):
			return False
		result.append(root)
		peopleDag.pop(root)
	for x in result:
		resultString+=str(x)
	print(str(resultString))
