class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):

        newNode = TreeNode(data)
        if (self.root == None):
            self.root = newNode
        else:
            currNode = self.root
            while True:
                if (data < currNode.val):
                    if (currNode.left == None):
                        currNode.left = newNode
                        return
                    else:
                        currNode = currNode.left
                elif (data > currNode.val):
                    if (currNode.right == None):
                        currNode.right = newNode
                        return
                    else:
                        currNode = currNode.right

class Solution:
    def flipEquiv(self , r1 : TreeNode , r2 : TreeNode):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        if r1.val != r2.val:
            return False
        return self.flipEquiv(r1.left , r2.left) and self.flipEquiv(r1.right , r2.right) or self.flipEquiv(r1.left , r2.right) and self.flipEquiv(r1.right , r2.left) 
root = Tree()
root.insert(1)
root.insert(2)
root.insert(3)
root.insert(4)
x = Solution()
print(x.flipEquiv(root.root , root.root))
