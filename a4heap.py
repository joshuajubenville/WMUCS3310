class MinHeap:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.size = 0
        self.heap = [(0, 0)] * (self.maxSize + 1)
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
            if (self.heap[pos][0] > self.heap[self.lc(pos)][0] or self.heap[pos][0] > self.heap[self.rc(pos)][0]):
                if self.heap[self.lc(pos)][0] < self.heap[self.rc(pos)][0]:
                    self.swap(pos, self.lc(pos))
                    self.minHeapify(self.lc(pos))
                else:
                    self.swap(pos, self.rc(pos))
                    self.minHeapify(self.rc(pos))
                
    def insert(self, priority, patientID):
        if self.size >= self.maxSize:
            raise Exception("Heap overflow.")
        self.size += 1
        self.heap[self.size] = (priority, patientID)
        current = self.size
        while self.heap[current][0] < self.heap[self.par(current)][0]:
            self.swap(current, self.par(current))
            current = self.par(current)

    def heapPrint(self):
        for i in range(1, (self.size // 2) + 1):
            parent = self.heap[i]
            lci = 2 * i
            rci = (2 * i) + 1
            print(" Parent: " + str(parent), end = "")
            if lci <= self.size: 
                print(" Left Child: " + str(self.heap[lci]), end = "")
            if rci <= self.size:                    
                print(" Right Child: " + str(self.heap[rci]), end = "")

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
    mh.insert(5, 5143)
    mh.insert(3, 6588)
    mh.insert(17, 6488)
    mh.insert(10, 1366)
    mh.insert(84, 2975)
    mh.insert(19, 9877)
    mh.insert(6, 642)
    mh.insert(22, 8944)
    mh.insert(9, 6234)
    mh.buildHeap()

    mh.heapPrint()
    print("The minimum value is " + str(mh.remove()[0]))