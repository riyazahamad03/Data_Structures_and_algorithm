
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.cnt = 0
        def dfs(node):
            if not node:
                return [0 , 0]    
            l = dfs(node.left)
            r = dfs(node.right)

            tot = l[0] + r[0] + node.val
            nodeCount = l[1] + r[1] + 1

            if tot//nodeCount == node.val:
                self.cnt += 1
            return [tot , nodeCount]
        dfs(root)
        return self.cnt
node = TreeNode(4)
node.left = TreeNode(8)
node.left.left = TreeNode(0)
node.left.right = TreeNode(1)
node.right = TreeNode(5)
node.right.right = TreeNode(6)
x = Solution()
print(x.averageOfSubtree(node))