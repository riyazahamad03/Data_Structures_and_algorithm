# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        q = collections.deque([root])
        res = []
        while q:
            maxVal = float("-inf")
            for i in range(len(q)):
                node = q.popleft()
                maxVal = max(maxVal, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(maxVal)
        return res


root = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right = TreeNode(2)
root.right.right = TreeNode(9)

x = Solution()
print(x.largestValues(root))
