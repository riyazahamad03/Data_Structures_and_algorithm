import heapq
import collections


class solution:
    def maxProbablity(self, n: int, edges: list[list[int]], succProb: list[int], start: int, end: int):
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src, succProb[i]])

        visit = set()
        pq = [(-1, start)]
        while pq:
            prob, path = heapq.heappop(pq)

            visit.add(path)
            if path == end:
                return float(prob * - 1)
            for nei, currSucc in adj[path]:
                if nei not in visit:
                    heapq.heappush(pq, (prob * currSucc, nei))
        return float(0)


x = solution()
print(x.maxProbablity(n=3, edges=[[0, 1], [1, 2], [
      0, 2]], succProb=[0.5, 0.5, 0.2], start=0, end=2))
