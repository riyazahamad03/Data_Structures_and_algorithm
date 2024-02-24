import collections


class Solution:
    def findAllPeople(
        self, n: int, meetings: list[list[int]], firstPerson: int
    ) -> list[int]:
        res = set([0, firstPerson])
        time = {}

        for src, dst, t in meetings:
            if t not in time:
                time[t] = collections.defaultdict(list)
            time[t][src].append(dst)
            time[t][dst].append(src)

        def dfs(src, adj):
            if src in visit:
                return
            visit.add(src)
            res.add(src)
            for nei in adj[src]:
                dfs(nei, adj)

        for t in sorted(time.keys()):
            visit = set()
            for src in time[t]:
                if src in res:
                    dfs(src, time[t])
        return list(res)


x = Solution()
print(x.findAllPeople(n=6, meetings=[[1, 2, 5], [2, 3, 8], [1, 5, 10]], firstPerson=1))
