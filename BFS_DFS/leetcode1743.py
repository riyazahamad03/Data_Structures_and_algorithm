import collections


class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        adj = collections.defaultdict(list)
        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)

        root = None

        for u in adj:
            if len(adj[u]) == 1:
                root = u

        visit, res = set([root]), []

        def dfs(node, prev):
            res.append(node)
            for nei in adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei, node)

        dfs(root, None)
        return res


x = Solution()
print(x.restoreArray([[2, 1], [3, 4], [3, 2]]))
