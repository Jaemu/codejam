import random

def sort(elems):
	if len(elems) <= 1:
		return elems
	else:
		pivot = random.choice(range(len(elems) - 1))
		compare = elems[pivot]
		lessThan = []
		greaterThan = []
		equalTo = []
		for i in xrange(len(elems)):
			if(elems[i] < compare):
				lessThan.append(elems[i])
			elif(elems[i] == compare):
				equalTo.append(elems[i])
			else:
				greaterThan.append(elems[i])
		lessThan = sort(lessThan)
		greaterThan = sort(greaterThan)
		return lessThan + equalTo + greaterThan