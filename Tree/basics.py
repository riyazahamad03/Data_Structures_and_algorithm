class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self,data):
        newNode = Node(data)
        if (self.root == None):
            self.root = newNode
        else:
            currNode = self.root
            while True:
                if (data < currNode.data):
                    if(currNode.left == None):
                        currNode.left = data
                        return
                    else:
                        currNode = currNode.left
                elif(data > currNode.data):
                    if(currNode.right == None):
                        currNode.right = data
                        return
                    else:
                        currNode = currNode.right
    def checkExist(self,data):
        curr = self.root
        while True:
            if curr == None:
                return False
            if curr.data == data:
                return True
            elif(data < curr.data):
                curr = curr.left
            else:
                curr = curr.right

bst = BinaryTree()
bst.insert(10)
print(bst.checkExist(10))
                