import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
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
    def minDepth(self, root: TreeNode):
        if not root:
            return 0
        q = collections.deque()
        q.append((root, 1))
        while q:
            for i in range(len(q)):
                node, length = q.popleft()
                if not node.left and not node.right:
                    return length
                if node.left:
                    q.append((node.left, length + 1))
                if node.right:
                    q.append((node.right, length + 1))


root = Tree()
root.insert(10)
root.insert(2)
root.insert(14)
root.insert(4)
root.insert(11)
root.insert(22)


x = solution()
print(x.minDepth(root.root))
