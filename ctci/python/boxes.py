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
		return self.height < other.height and self.width < other.width and self.depth < other.depth

cache = {}

def getMaxTowers(boxes, bottom):
	global cache
	if bottom is None:
		return []
	if boxes is None or len(boxes) == 0:
		return [bottom]
	if len(boxes) == 1:
		if(boxes[0] < bottom):
			return [bottom, boxes[0]]
		else:
			return [bottom]
	maxTower = [bottom]
	maxHeight = 0
	for i in xrange(len(boxes)):
		if boxes[i] < bottom:
			tower = [bottom] + getMaxTowers(boxes[i:], boxes[i])
			currentHeight = 0
			for b in tower:
				currentHeight = currentHeight + b.height
			if currentHeight > maxHeight:
				maxHeight = currentHeight
				maxTower = tower
	return maxTower



def getMaxTower(boxes):
	towers = {}
	if len(boxes) <= 1:
		return [boxes]
	maxTower = []
	for box in boxes:
		towers[box] = getMaxTowers(boxes, box)
		if len(towers[box]) > len(maxTower):
			maxTower = towers[box]
	print(towers)
	return maxTower

def main():
	boxes = []
	for i in xrange(10):
		width = random.randint(1,50)
		height = random.randint(width,50)
		depth = random.randint(1,30)
		boxes.append(Box(height,width,depth))
	boxes.sort(key=lambda x: x.height, reverse=True)
	result = getMaxTower(boxes)
	print('Boxes: ')
	for i in boxes:
		print(i)
	print("Max tower")
	for i in result:
		print(i)


if __name__ == '__main__':
	main()