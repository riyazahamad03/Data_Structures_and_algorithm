from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int):
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        if not root:
            return None

        q = deque()
        q.append(root)

        level = 1
        while level < depth - 1:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        while q:
            node = q.popleft()
            left_child = TreeNode(val)
            right_child = TreeNode(val)

            left_child.left = node.left
            right_child.right = node.right

            node.left = left_child
            node.right = right_child

        return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)

x = Solution()
print(x.addOneRow(root, 1, 2))
