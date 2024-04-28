import collections


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        res = [0] * (n)
        cnt = [1] * (n)
        self.root = 0

        def dfs(curr, par, depth):
            out = 1
            for ch in graph[curr]:
                if ch != par:
                    out += dfs(ch, curr, depth + 1)
                    self.root += depth + 1
            cnt[curr] = out
            return out

        dfs(0, -1, 0)

        def dfs2(curr, par, ans):
            res[curr] = ans
            for ch in graph[curr]:
                if ch != par:
                    dfs2(ch, curr, ans + (n - cnt[ch]) - cnt[ch])

        dfs2(0, -1, self.root)
        return res


x = Solution()
print(x.sumOfDistancesInTree(n=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
