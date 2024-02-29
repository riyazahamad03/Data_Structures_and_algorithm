# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        q = deque([root])
        level = 0
        while q:
            prev = None
            for i in range(len(q)):
                node = q.popleft()
                if prev:
                    if level % 2 == 0:
                        if not ((node.val % 2) and (node.val > prev)):
                            return False
                    elif level % 2:
                        if not (node.val % 2 == 0 and node.val < prev):
                            return False
                else:
                    if level % 2 == 0 and node.val % 2 == 0:
                        return False
                    elif level % 2 and node.val % 2:
                        return False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                prev = node.val
            level += 1
        return True


root = TreeNode(1)
root.left = TreeNode(10)
root.right = TreeNode(4)
root.left.left = TreeNode(3)


x = Solution()
print(x.isEvenOddTree(root))
