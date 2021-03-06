class Heap:
	def __init__(self, isMin=True):
		self.items = []
		self.isMin = isMin

	def insert(self, elem):
		self.items.append(elem)
		currentIndex = len(self.items) - 1
		if(len(self.items) == 1):
			return
		indexOfParent = ((currentIndex)/2)
		self.heapify()

	def heapify(self):
		currentIndex = len(self.items) - 1
		parentIndex = (currentIndex/2)
		while(currentIndex > -1 and parentIndex > -1):
			if(self.isMin):
				if(self.items[currentIndex] < self.items[parentIndex]):
					self.items[currentIndex] = self.items[currentIndex] + self.items[parentIndex]
					self.items[parentIndex] = self.items[currentIndex]  - self.items[parentIndex]
					self.items[currentIndex] =  self.items[currentIndex]  - self.items[parentIndex]
			else:
				if(self.items[currentIndex] > self.items[parentIndex]):
					self.items[currentIndex] = self.items[currentIndex] + self.items[parentIndex]
					self.items[parentIndex] = self.items[currentIndex]  - self.items[parentIndex]
					self.items[currentIndex] =  self.items[currentIndex]  - self.items[parentIndex]
			currentIndex = currentIndex - 1
			parentIndex = (currentIndex/2)
		print(self.items)

	def getRoot(self):
		if(len(self.items) == 0):
			print('Heap is empty')
			return
		root = self.items[0]
		self.items[0] = self.items[len(self.items) - 1]
		remove = self.items.pop()
		print(self.items)
		self.heapify()
		return root


def main():
	maxHeap = Heap(False)
	maxHeap.insert(3)
	maxHeap.insert(5)
	maxHeap.insert(10)
	maxHeap.insert(6)
	maxHeap.insert(20)
	print(maxHeap.items)


if __name__ == '__main__':
	main()