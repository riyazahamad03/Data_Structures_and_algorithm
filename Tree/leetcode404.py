# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        lSum = 0
        q = collections.deque([(root, "r")])
        while q:
            for _ in range(len(q)):
                node, pos = q.popleft()
                if pos == "l" and not node.left and not node.right:
                    lSum += node.val

                if node.left:
                    q.append((node.left, "l"))
                if node.right:
                    q.append((node.right, "r"))
        return lSum


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

x = Solution()
print(x.sumOfLeftLeaves(root))
