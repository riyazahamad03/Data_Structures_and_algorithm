class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, mx, mi):
            if not node:
                return
            if node.left:
                nonlocal res
                res = max(res, abs(mx - node.left.val), abs(mi - node.left.val))
                dfs(node.left, max(mx, node.left.val), min(mi, node.left.val))
            if node.right:
                res = max(res, abs(mx - node.right.val), abs(mi - node.right.val))
                dfs(node.right, max(mx, node.right.val), min(mi, node.right.val))

        dfs(root, root.val, root.val)
        return res


root = TreeNode(8)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)


root.right = TreeNode(10)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)


x = Solution()
print(x.maxAncestorDiff(root))
