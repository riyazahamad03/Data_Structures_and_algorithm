import collections


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
        if self.root is None:
            self.root = newNode
        else:
            currNode = self.root
            while True:
                if data < currNode.val:
                    if currNode.left is None:
                        currNode.left = newNode
                        break
                    else:
                        currNode = currNode.left
                elif data > currNode.val:
                    if currNode.right is None:
                        currNode.right = newNode
                        break
                    else:
                        currNode = currNode.right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        res, q = 0, collections.deque()
        q.append([root, 0])
        while q:
            qLen, lMin, rMax = len(q), float('inf'), float('-inf')
            for _ in range(qLen):
                node, num = q.popleft()
                lMin, rMax = min(lMin, num), max(rMax, num)
                if node.left:
                    q.append([node.left, num * 2])
                if node.right:
                    q.append([node.right, num * 2 + 1])

            res = max(res, (rMax - lMin) + 1)

        return res


tree = Tree()
tree.insert(10)
tree.insert(5)
tree.insert(20)
tree.insert(49)
tree.insert(2)

x = Solution()
print(x.widthOfBinaryTree(tree.root))
