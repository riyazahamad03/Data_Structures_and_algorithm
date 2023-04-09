class TreeNode:
    def __init__(self, data):
        self.val = data
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
    def diametreOfBinTree(self , root:TreeNode):
        res = float('-inf')
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            res = max(res , l + r)
            return 1 + max(l , r)
        dfs(root)
        return res
    

root = Tree()
root.insert(1)
root.insert(2)
root.insert(3)
root.insert(4)
x = Solution()
print(x.diametreOfBinTree(root.root))