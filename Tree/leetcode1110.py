# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete: int):
        res_set = set([root])
        to_delete = set(to_delete)

        def dfs(node):
            if not node:
                return None
            res = node
            if node.val in to_delete:
                res = None
                res_set.discard(node)
                if node.left:
                    res_set.add(node.left)
                if node.right:
                    res_set.add(node.right)
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return res

        dfs(root)
        return list(res_set)


x = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(4)
print(x.delNodes(root, [2]))
