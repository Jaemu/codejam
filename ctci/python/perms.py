
def getPerms(input):
	perms = []
	if(input is None):
		return None
	if(len(input) == 0):
		perms.append('')
		return perms
	if(len(input) == 1):
		return [input]
	firstChar = input[0]
	remainder = input[1:]
	remainderPerms = getPerms(remainder)
	for i in xrange(len(remainderPerms)):
		for j in xrange(len(remainderPerms[i]) + 1):
			temp = remainderPerms[i][0:j] + firstChar + remainderPerms[i][j:]
			perms.append(temp)
	return perms


if __name__ == '__main__':
	testString = 'abc';
	print(getPerms(testString));