def testReplace(longer, shorter, index):
	test = shorter[:index-1] + longer[index] + shorter[index:]
	print('Test replace: test = ' + test+ ', longer = ' + longer + ', index = ' + str(index))
	return shorter == test

def testDelete(longer, shorter, index):
	test = longer[:(index-1)] + longer[index:]
	print('Test delete: test = ' + test+ ', longer = ' + longer  + ', index = ' + str(index))
	return shorter == test

def testInsert(longer, shorter, index):
	test = shorter[:index] + longer[index] + shorter[index:]
	print('Test insert: test = ' + test + ', longer = ' + longer + ', index = ' + str(index))
	return test == longer

def testInput(longer, shorter, index):
	return testInsert(longer, shorter, index) or testDelete(longer,shorter,index) or testReplace(longer,shorter, index)

def isOneAway(a, b):
	shorter = ''
	longer = ''
	if(len(a) == len(b) or len(a) == (len(b) + 1)):
		shorter = b
		longer = a
	elif(len(b) == (len(a) + 1)):
		shorter = a
		longer = b
	else:
		return False
	numEdits = 0
	for index in xrange(len(shorter)):
		if(shorter[index] is not longer[index]):
			if(testInput(longer, shorter, index)):
				numEdits = numEdits + 1
	return numEdits <= 1
