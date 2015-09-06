def testReplace(longer, shorter, index):
	shorter[index] = shorter[:index-1] + longer[index] + shorter[index:]
	return shorter is longer

def testDelete(longer, shorter, index):
	shorter = shorter[:(index-1)] + shorter[index:]
	return shorter is longer

def testInsert(longer, shorter, index):
	shorter = shorter[:index] + longer[index] + shorter[index:]
	return shorter is longer

def testInput(longer, shorter, index):
	return testInsert(longer, shorter, index) or testDelete(longer,shorter,index) or testReplace(longer,shorter, index)

def isOneAway(a, b):
	shorter = ''
	longer = ''
	if(len(a) == len(b)):
		return True
	if(len(a) > len(b)):
		shorter = b
		longer = a
	else:
		shorter = a
		longer = b
	for index in xrange(len(longer)):
		if(longer[index] is not shorter[index]):
			return testInput(longer, shorter, index)

