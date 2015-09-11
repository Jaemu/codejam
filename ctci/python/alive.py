#Given a list of person objects with birth and death defined
#Find year with max num people alive
import random

class Person:
	def __init__(self, birth=None, death=None):
		self.birth = birth
		self.death = death

def makePeopleList():
	result = []
	for i in xrange(100):
		birth = random.randint(1900, 2000)
		death = random.randint(birth, 2000)
		person = Person(birth, death)
		result.append(person)
	return result




def getMaxNumPeopleAlive():
	people = makePeopleList()
	numPeopleAlive = []
	for i in xrange(101):
		currentNumPeople = ([x for x in people if x.birth <= (1900 + i) and x.death > (1900 + i)])
		numPeopleAlive.append(currentNumPeople)

	return numPeopleAlive.index(max(numPeopleAlive)) + 1900

def main():
	print(getMaxNumPeopleAlive())

if __name__ == '__main__':
	main()