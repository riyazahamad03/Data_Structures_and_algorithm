class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def isValid(Map):
            oddCount = 0
            for i in Map:
                if Map[i] % 2 != 0:
                    oddCount += 1
                if oddCount > 1:
                    return 0
            return 1

        res = 0

        def dfs(node, Map):
            if not node:
                return
            Map[node.val] = 1 + Map.get(node.val, 0)
            if not node.left and not node.right:
                nonlocal res
                res += isValid(Map)
                return
            dfs(node.left, dict(Map))
            dfs(node.right, dict(Map))

        dfs(root, {})
        return res


root = TreeNode(2)
root.left = TreeNode(3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right = TreeNode(1)
root.right.right = TreeNode(1)


x = Solution()
print(x.pseudoPalindromicPaths(root))
