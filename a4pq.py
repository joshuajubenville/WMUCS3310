class pqNode:
    def __init__(self, pr, data, nx = None):
        self.data = data
        self.pr = pr
        self.nx = nx

class PriorityQueue:
    def __init__(self):
        self.front = None

    def isEmpty(self):
        return True if self.front == None else False
    
    def push(self, pr, data):
        pr = int(pr)
        if self.isEmpty():
            self.front = pqNode(pr, data)
            return 1
        else:
            if self.front.pr > pr:
                newNode = pqNode(pr, data)
                newNode.nx = self.front
                self.front = newNode
                return 1
            else:
                temp = self.front
                while temp.nx:
                    if pr <= temp.nx.pr:
                        break
                    temp = temp.nx
                newNode = pqNode(pr, data)
                newNode.nx = temp.nx
                temp.nx = newNode
                return 1
    
    def pop(self):
        if self.isEmpty():
            raise Exception("The queue is empty!")
        else:
            self.front = self.front.nx
            return 1
        
    def peek(self):
        if self.isEmpty():
            raise Exception("The queue is empty!")
        else:
            return self.front.data
        
    def traverse(self):
        if self.isEmpty():
            raise Exception("The queue is empty!")
        else:
            temp = self.front
            while temp:
                print(temp.data, end = " ")
                temp = temp.nx

    def search(self, key):
        if self.isEmpty():
            raise Exception("The queue is empty!")
        else:
            search = self.front
            while search:
                if search.pr == key:
                    print(search.data, end = " ")
                search = search.nx

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push(8, 75866)
    pq.push(3, 16788)
    pq.push(3, 64788)
    pq.push(4, 23196)
    pq.push(0, 65245)

    pq.traverse()
    pq.pop()
    pq.traverse()
    print("\n")
    pq.search(2)