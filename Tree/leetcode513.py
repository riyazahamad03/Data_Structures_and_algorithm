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


class solution:
    def findBottomLeft(self, root: TreeNode):
        q = collections.deque()
        q.append(root)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return node.val


root = Tree()
root.insert(1)
root.insert(2)
root.insert(3)
root.insert(4)

x = solution()
print(x.findBottomLeft(root.root))
