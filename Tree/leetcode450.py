class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def __init__(self) -> None:
        self.root = None
    def insert(self,val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            currNode = self.root
            newNode = TreeNode(val)
            while True:
                if val < currNode.val:
                    if(currNode.left == None):
                        currNode.left = newNode
                        break
                    else:
                        currNode = currNode.left
                elif val > currNode.val:
                    if currNode.right == None:
                        currNode.right = newNode
                        break
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
            elif data > root.root.right:
                root.root = root.root.right



class solution:
    def deleteNode(self,root:TreeNode,key:int):
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            currNode = root.right
            while currNode.left:
                currNode = currNode.left
            root.val = currNode.val
            root.right = self.deleteNode(root.right,root.val)
        return root
    


root = Tree()
root.insert(10)
root.insert(5)
root.insert(3)
root.insert(12)
root.insert(15)

x = solution()
print(x.deleteNode(root.root,3))
print(root.lookup(3))