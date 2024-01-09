class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leftSimilar(self, root1: Node, root2: Node):
        def dfs(node, leaf):
            if not node:
                return
            if not node.left and not node.right:
                leaf.append(node.val)
            dfs(node.left, leaf)
            dfs(node.right, leaf)
            return leaf

        leaf_1 = dfs(root1, [])
        leaf_2 = dfs(root2, [])

        return leaf_1 == leaf_2


x = Node(5)
x.left = Node(3)
x.right = Node(4)

y = Node(4)
y.left = Node(3)
y.right = Node(4)


sol = Solution()
print(sol.leftSimilar(x, y))
