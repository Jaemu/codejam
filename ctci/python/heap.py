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
			if(currentIndex == parentIndex):
				return
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



def main():
	heap = Heap(False)
	heap.insert(3)
	heap.insert(5)
	heap.insert(10)
	heap.insert(6)
	heap.insert(20)
	print(heap.items)


if __name__ == '__main__':
	main()