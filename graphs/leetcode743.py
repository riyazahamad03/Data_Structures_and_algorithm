import collections
import heapq


class solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int):
        adj = {i: [] for i in range(n)}
        for u, v, w in times:
            adj[u].append((v, w))

        minHeap = [(0, k)]
        res = 0
        visit = set()
        while minHeap:
            weight, node = heapq.heappop(minHeap)

            if node in visit:
                continue
            visit.add(node)
            res = max(res, weight)

            if len(visit) == n:
                return res

            for newNode, newWeight in adj[node]:
                if newNode not in visit:
                    heapq.heappush(minHeap, (newWeight + weight, newNode))
        return - 1


x = solution()
print(x.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
