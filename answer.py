def unique(code, codes):
	reverse = code[::-1]
	if(code == reverse):
		return codes.count(code) is 1
	return (codes.count(code) is 1) and (codes.count(reverse) is 0)

def answer(x):
	result = []
	while(len(x) > 0):
		current = x[0]
		reverse = current[::-1]
		x = [value for value in x if value != current and value != reverse]
		result.append(current)
	return result