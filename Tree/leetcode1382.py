# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inOrder(self, root, in_order_list):
        if not root:
            return
        self.inOrder(root.left, in_order_list)
        in_order_list.append(root.val)
        self.inOrder(root.right, in_order_list)

    def createBalancedTree(self, lst, start, end):
        if start > end:
            return None
        mid = (start + end) // 2

        left = self.createBalancedTree(lst, start, mid - 1)
        right = self.createBalancedTree(lst, mid + 1, end)
        node = TreeNode(lst[mid], left, right)
        return node

    def balanceBST(self, root: TreeNode) -> TreeNode:
        in_order_list = []
        self.inOrder(root, in_order_list)
        return self.createBalancedTree(in_order_list, 0, len(in_order_list) - 1)


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(6)
x = Solution()
print(x.balanceBST(root))
