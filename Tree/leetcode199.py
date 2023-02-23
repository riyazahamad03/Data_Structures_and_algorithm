import collections
class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def insert(self,data):
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

class Solution:
    def rightSideView(self,root:TreeNode):
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            rightSide = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res    


root = Tree()
root.insert(10)
root.insert(20)
root.insert(49)
root.insert(2)

x = Solution()
print(x.rightSideView(root.root))
