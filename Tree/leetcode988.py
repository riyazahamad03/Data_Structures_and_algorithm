# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def dfs(node, curr):
            if not node:
                return
            curr = chr(ord("a") + node.val) + curr
            if node.left and node.right:
                return min(dfs(node.left, curr), dfs(node.right, curr))
            if node.left:
                return dfs(node.left, curr)
            if node.right:
                return dfs(node.right, curr)
            return curr

        return dfs(root, "")


root = TreeNode(0)
root.left = TreeNode(5)
root.right = TreeNode(4)
x = Solution()
print(x.smallestFromLeaf(root))
