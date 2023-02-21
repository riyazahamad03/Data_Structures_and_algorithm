import collections
class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def __init__(self) -> None:
        self.root = None
    def insert(self,val):
        newNode = TreeNode(val)
        if not self.root:
            self.root = newNode
        else:
            curr = self.root
            while True:
                if val < curr.val:
                    if curr.left == None:
                        curr.left = newNode
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right == None:
                        curr.right = newNode
                        break
                    else:
                        curr = curr.right

class solution:
    def levelOrderTraversal(self,root:TreeNode):
        q = collections.deque()
        res = []
        if root:
            q.append(root)
        while q:
            val = []
            for idex in range(len(q)):
                qRoot = q.popleft()
                val.append(qRoot.val)
                if qRoot.left:
                    q.append(qRoot.left)
                if qRoot.right:
                    q.append(qRoot.right)
            res.append(val)
        return res
        
root = Tree()
root.insert(10)
root.insert(2)
root.insert(14)
root.insert(4)
root.insert(11)
root.insert(22)

x = solution()
print(x.levelOrderTraversal(root.root))