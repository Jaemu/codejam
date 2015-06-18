lookupTable = []

def genLookupTable():
	result = []
	for i in xrange(101):
		result.append(i * i)
	return result


def answerHelper(n, value):
	if n <= 1:
		return value
	else:
		i = 0
		while i < len(lookupTable) and lookupTable[i] <= n:
			i = i + 1
		i = i - 1
	result = n - lookupTable[i]
	return answerHelper(result, value + 1)
	

def answer(n):
	global lookupTable
	lookupTable = genLookupTable()
	return answerHelper(n, 0)