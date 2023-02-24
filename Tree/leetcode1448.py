class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def insertNodes(self,data):
        newNode = TreeNode(data)
        if not self.root:
            self.root = newNode
        else:
            cur = self.root
            while True:
                if data < cur.val:
                    if cur.left == None:
                        cur.left = newNode
                        break
                    else:
                        cur = cur.left
                elif data > cur.val:
                    if cur.right == None:
                        cur.right = newNode
                        break
                    else:
                        cur = cur.right
class solution:
    def goodNodes(self,root:TreeNode):
        def dfs(node,maxVal):
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0

            maxVal = max(maxVal,node.val)

            res += dfs(node.left,maxVal)
            res += dfs(node.right,maxVal)

            return res
        return dfs(root,root.val)


root = Tree()
root.insertNodes(10)
root.insertNodes(20)
root.insertNodes(12)
root.insertNodes(5)
root.insertNodes(15)
root.insertNodes(21)
root.insertNodes(55)

x = solution()
print(x.goodNodes(root.root))