class TreeNode:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None
        

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,data):

        newNode = TreeNode(data)
        if (self.root == None):
            self.root = newNode
        else:
            currNode = self.root
            while True:
                if (data < currNode.val):
                    if(currNode.left == None):
                        currNode.left = newNode
                        return
                    else:
                        currNode = currNode.left
                elif(data > currNode.val):
                    if(currNode.right == None):
                        currNode.right = newNode
                        return
                    else:
                        currNode = currNode.right
    def lookup(self,data):
        while True:
            if not root.root:
                return False
            if root.root.val == data:
                return True
            if data < root.root.val:
                root.root = root.root.left
            else:
                root.root = root.root.right
                        
        
        
class solution:
    def insertIntoBst(self,root:TreeNode,val:int):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBst(root.left,val)
        else:
            root.right = self.insertIntoBst(root.right,val)
        return root
root = Tree()
root.insert(10)
root.insert(5)
root.insert(20)
root.insert(50)


x=solution()
print(x.insertIntoBst(root.root,500))

print(root.lookup(500))