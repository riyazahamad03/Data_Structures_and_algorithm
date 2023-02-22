class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def __init__(self) -> None:
        self.root = None
    def insert(self,data):
        newNode = TreeNode(data)
        if not self.root:
            self.root = newNode
        else:
            curr = self.root
            while True:
                if data < curr.val:
                    if curr.left == None:
                        curr.left = newNode
                        break
                    else:
                        curr = curr.left
                elif data > curr.val:
                    if curr.right == None:
                        curr.right = newNode
                        break
                    else:
                        curr = curr.right

class solution:
    def sumNumbers(self,root:TreeNode):
        def dfs(cur,rLeafVal):
            if not cur:
                return 0
            rLeafVal = rLeafVal * 10 + cur.val
            if (not cur.left and not cur.right):
                return rLeafVal
            return dfs(cur.left,rLeafVal) + dfs(cur.right,rLeafVal)
        return dfs(root,0)
        

root = Tree()
root.insert(10)
root.insert(2)
root.insert(14)
root.insert(4)
root.insert(11)
root.insert(22)
root.insert(12)
x = solution()
print(x.sumNumbers(root.root))