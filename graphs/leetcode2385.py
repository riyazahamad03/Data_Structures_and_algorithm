from collections import deque
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        adj = defaultdict(list)
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)
                q.append(node.left)
            if node.right:
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)
                q.append(node.right)
        q = deque([start])
        res = -1
        visit = set([start])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for elem in adj[node]:
                    if elem not in visit:
                        visit.add(elem)
                        q.append(elem)
            res += 1
        return res


root = TreeNode(1)
root.left = TreeNode(5)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(9)
root.left.right.left = TreeNode(2)


root.right = TreeNode(3)
root.right.left = TreeNode(10)
root.right.right = TreeNode(6)

x = Solution()
print(x.amountOfTime(root, 3))
