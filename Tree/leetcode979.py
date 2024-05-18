
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
            l_extra = dfs(curr.left)
            r_extra = dfs(curr.right)

            extra = l_extra + r_extra + curr.val - 1
            self.res += abs(extra)
            return extra

        dfs(root)
        return self.res


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(2)

x = Solution()
print(x.distributeCoins(root))
