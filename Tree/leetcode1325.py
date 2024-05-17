# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int):
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None
        return root


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(5)
x = Solution()
print(x.removeLeafNodes(root, 5))
