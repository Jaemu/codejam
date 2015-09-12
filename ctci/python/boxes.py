import random
class Box:
	def __init__(self, height=0,width=0,depth=0):
		self.height = height
		self.width = width
		self.depth = depth

	def __hash__(self):
		return hash(repr(self))

	def __str__(self):
		return str('Box: height - ' + str(self.height) + ', width - ' + str(self.width) + ', depth - ' + str(self.depth))

	def __lt__(self, other):
		return self.height <= other.height and self.width < other.width and self.depth < other.depth

def getMaxTowers(boxes, bottom):
	if bottom is None:
		return []
	if boxes is None or len(boxes) == 0:
		return [bottom]
	#if bottom in cache.keys():
	#	return cache[bottom]
	maxTower = [bottom]
	maxHeight = 0
	for i in xrange(len(boxes)):
		tower = [bottom] 
		if boxes[i] < bottom:
			tower = tower + getMaxTowers(boxes[i:], boxes[i])
			currentHeight = 0
			for b in tower:
				currentHeight = currentHeight + b.height
			print('Current: ' + str(currentHeight) + ', max: ' + str(maxHeight))
			if currentHeight > maxHeight:
				maxHeight = currentHeight
				maxTower = tower
	return maxTower



def getMaxTower(boxes):
	towers = []
	maxHeight = 0
	maxTower = 0
	if len(boxes) <= 1:
		return [boxes]
	for box in boxes:
		towers.append(getMaxTowers(boxes, box))
	for tower in towers:
		currentHeight = 0
		for box in tower:
			currentHeight = currentHeight + box.height
		if(currentHeight > maxHeight):
			maxHeight = currentHeight
			maxTower = towers.index(tower)
	return towers[maxTower]

def main():
	global cache
	boxes = []
	for i in xrange(5):
		width = random.randint(1,50)
		height = random.randint(width,50)
		depth = random.randint(1,30)
		boxes.append(Box(height,width,depth))
	boxes.sort(key=lambda x: x.height, reverse=True)
	result = getMaxTower(boxes)
	print('Boxes: ')
	for i in boxes:
		print(i)
	print('Max Tower: ')
	for i in result:
		print(i)


if __name__ == '__main__':
	main()