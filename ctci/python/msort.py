
def msort(items):
	if(items is None):
		return []
	if(len(items) == 1):
		return items
	else:
		breakpoint = len(items)/2
		return merge(msort(items[:breakpoint]), msort(items[breakpoint:]))

def merge(items1, items2):
	result = []
	while(len(items1) > 0 and len(items2) > 0):
		if(items1[0] <= items2[0]):
			result.append(items1.pop(0))
		else:
			result.append(items2.pop(0))
	if(len(items1) > 0):
		result = result + items1
	else:
		result = result + items2
	return result

def main():
	print(msort([4,2,5,7,8,9,2,5,3]))

if __name__ == '__main__':
	main()