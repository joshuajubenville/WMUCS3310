class MinHeap:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.size = 0
        self.heap = [0] * (self.maxSize + 1)
        self.front = 1

    def par(self, pos): # par = parent
        return pos // 2
    
    def lc(self, pos): # lc = left child
        return 2 * pos
    
    def rc(self, pos): # rc = right child
        return (2 * pos) + 1
    
    def isLeaf(self, pos):
        return pos * 2 > self.size
    
    def swap(self, first, second):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.heap[pos] > self.heap[self.lc(pos)] or self.heap[pos] > self.heap[self.rc(pos)]):
                if self.heap[self.lc(pos)] < self.heap[self.rc(pos)]:
                    self.swap(pos, self.lc(pos))
                    self.minHeapify(self.lc(pos))
                else:
                    self.swap(pos, self.rc(pos))
                    self.minHeapify(self.rc(pos))
                
    def insert(self, thing):
        if self.size >= self.maxSize:
            raise Exception("Heap overflow.")
        self.size += 1
        self.heap[self.size] = thing
        current = self.size
        while self.heap[current] < self.heap[self.par(current)]:
            self.swap(current, self.par(current))
            current = self.par(current)

    def heapPrint(self):
        for i in range(1, (self.size // 2) + 1):
            print(" Parent: " + str(self.heap[i]) + 
                  " Left Child: " + str(self.heap[2 * i]) +
                  " Right Child: " + str(self.heap[(2 * i) + 1]))

    def buildHeap(self):
        for pos in range(self.size // 2, 0 , -1):
            self.minHeapify(pos)

    def remove(self):
        popped = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.minHeapify(self.front)
        return popped
    
if __name__ == "__main__":

    mh = MinHeap(15)
    mh.insert(5)
    mh.insert(3)
    mh.insert(17)
    mh.insert(10)
    mh.insert(84)
    mh.insert(19)
    mh.insert(6)
    mh.insert(22)
    mh.insert(9)
    mh.buildHeap()

    mh.heapPrint()
    print("The minimum value is " + str(mh.remove()))