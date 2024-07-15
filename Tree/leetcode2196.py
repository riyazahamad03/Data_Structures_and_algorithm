# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]):
        nodes = {}
        childrens = set()
        for parent, children, is_left in descriptions:
            childrens.add(children)
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if children not in nodes:
                nodes[children] = TreeNode(children)
            if is_left:
                nodes[parent].left = nodes[children]
            else:
                nodes[parent].right = nodes[children]
        for p, c, l in descriptions:
            if p not in childrens:
                return nodes[p]


x = Solution()
print(
    x.createBinaryTree(
        [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
    )
)
