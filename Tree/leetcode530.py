class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        newNode = TreeNode(data)
        if not self.root:
            self.root = newNode
        else:
            currNode = self.root
            while True:
                if data < currNode.data:
                    if not currNode.left:
                        currNode.left = newNode
                        break
                    currNode = currNode.left
                elif data > currNode.data:
                    if not currNode.right:
                        currNode.right = newNode
                        break
                    currNode = currNode.right


class Solution:
    def getMinimumDifference(self, root: TreeNode):
        prev, res = None, float("inf")

        def inOrder(node):

            if not node:
                return

            inOrder(node.left)

            nonlocal res, prev
            if prev:
                res = min(res, node.data - prev.data)
            prev = node

            inOrder(node.right)
        inOrder(root)
        return res


root = Tree()
root.insert(10)
root.insert(20)
root.insert(49)
root.insert(2)

x = Solution()
print(x.getMinimumDifference(root.root))
