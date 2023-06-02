import math


class solution:
    def maximumDetonation(self, bombs: list[list[int]]):
        adj = {i: [] for i in range(len(bombs))}
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

                if d <= r1:
                    adj[i].append(j)
                if d <= r2:
                    adj[j].append(i)

        def dfs(idex, visit):
            if idex in visit:
                return 0
            visit.add(idex)
            for nei in adj[idex]:
                dfs(nei, visit)
            return len(visit)
        res = 0
        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))
        return res


x = solution()
print(x.maximumDetonation([[2, 1, 3], [6, 1, 4]]))
