# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)

            if node.left and node.right:
                if node.val == 2:
                    res = node.left.val or node.right.val
                else:
                    res = node.left.val and node.right.val

                node.val = 1 if res else 0

        # dfs(root)
        # return root.val
        def dfs(node):
            if not node:
                return False
            if node.val in [0, 1]:
                return bool(node.val)

            left = dfs(node.left)
            right = dfs(node.right)

            if node.val == 2:
                return left or right
            elif node.val == 3:
                return left and right

        return dfs(root)


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(0)
x = Solution()
print(x.evaluateTree(root))
