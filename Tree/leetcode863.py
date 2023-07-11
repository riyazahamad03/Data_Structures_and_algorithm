import collections


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        newNode = TreeNode(data)
        if not self.root:
            self.root = newNode
        else:
            currNode = self.root
            while True:
                if data < currNode.data:
                    if not currNode.left:
                        currNode.left = newNode
                        break
                    currNode = currNode.left
                elif data > currNode.data:
                    if not currNode.right:
                        currNode.right = newNode
                        break
                    currNode = currNode.right


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        q = collections.deque([(target.data, 0)])
        visited = set([target.data])

        def buildGraph(node, par):
            if node and par:
                adj[node.data].append(par.data)
                adj[par.data].append(node.data)
            if node.left:
                buildGraph(node.left, node)
            if node.right:
                buildGraph(node.right, node)
        adj = collections.defaultdict(list)
        buildGraph(root, None)

        res = []

        while q:
            node, length = q.popleft()

            if length == k:
                res.append(node)

            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, length + 1))
        return res


root = Tree()
root.insert(10)
root.insert(20)
root.insert(49)
root.insert(2)


x = Solution()
print(x.distanceK(root.root, root.root, 1))
