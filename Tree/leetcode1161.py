import collections


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


class solution:
    def maxLevelSum(self, root: TreeNode):
        level, maxLevel, maxSum = 1, 0, float("-inf")
        q = collections.deque()
        q.append(root)
        while q:
            Sum = 0
            for i in range(len(q)):
                node = q.popleft()
                Sum += node.data

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if Sum > maxSum:
                maxSum, maxLevel = Sum, level
            level += 1
        return maxLevel


root = Tree()
root.insert(1)
root.insert(2)
root.insert(3)
root.insert(4)

x = solution()
print(x.maxLevelSum(root.root))