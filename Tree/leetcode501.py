# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
class Solution:
    def findMode(self, root: TreeNode):
        d = collections.defaultdict(int)
        def dfs(node):
            if not node:
                return 
            d[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        mxCnt = max(d.values())
        res = []
        for i in d:
            if d[i] == mxCnt:
                res.append(i)
        return res
    
node = TreeNode(1)
node.right = TreeNode(2)
node.right.left = TreeNode(2)

x = Solution()
print(x.findMode(node))
