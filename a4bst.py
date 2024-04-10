class bstNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.lc = None
        self.rc = None

    def __repr__(self):
        return f"({self.key}, {self.val})"
    
    def __getitem__(self, index):
        if index == 0:
            return self.key
        elif index == 1:
            return self.val
        else:
            raise IndexError("Index out of range")

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key, val):
        if self.root is None:
            self.root = bstNode(key, val)
        else:
            self.insertR(self.root, key, val)

    def insertR(self, node, key, val):
        if key < node.key:
            if node.lc is None:
                node.lc = bstNode(key, val)
            else:
                self.insertR(node.lc, key, val)
        elif key > node.key:
            if node.rc is None:
                node.rc = bstNode(key, val)
            else:
                self.insertR(node.rc, key, val)
        else:
            node.val = val

    def inorder(self):
        result = []
        self.inorderR(self.root, result)
        return result
    
    def inorderR(self, node, result):
        if node:
            self.inorderR(node.lc, result)
            result.append((node.key, node.val))
            self.inorderR(node.rc, result)

    def search(self, key):
        return self.searchR(self.root, key)
    
    def searchR(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self.searchR(node.lc, key)
        return self.searchR(node.rc, key)

if __name__ == "__main__":

    data = [(5, ["animal", "Joshua Jubenville"]), (1, ["plant"]), (15, ["fungi"])]

    bst = BinarySearchTree()
    for key, val in data:
        bst.insert(key, val)

    print(bst.inorder())

    searchKey = 5
    resultNode = bst.search(searchKey)
    if resultNode:
        print(f"Found node with key {searchKey}: {resultNode}")
    else:
        print(f"No node found with key {searchKey}")

    print(resultNode[1][1])

    