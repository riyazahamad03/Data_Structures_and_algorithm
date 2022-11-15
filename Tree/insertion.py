from collections import deque

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
class BinSearchTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        NewNode = Node(data)
        if(self.root == None):
            self.root = NewNode
            return self
        else:
            currNode = self.root
            while(True):
                if(data<currNode.data):
                    if(currNode.left == None):
                        currNode.left = NewNode
                        return
                    else:
                        currNode=currNode.left
                elif (data>currNode.data):
                    if(currNode.right == None):
                        currNode.right = NewNode
                        return
                    else:
                        currNode = currNode.right
    def lookup(self,data):
        currNode = self.root
        while(True):
            if(currNode == None):
                return False
            if(currNode.data == data):
                return True
            elif(data<currNode.data):
                currNode = currNode.left
            else:
                currNode = currNode.right

    def printt(self,curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.data))
            self.printt(curr_node.right)
    def print_tree(self):
        if self.root != None:
            self.printt(self.root)
    
bst = BinSearchTree()
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(10)
bst.insert(5)
bst.insert(22)
bst.insert(25)

bst.print_tree()

