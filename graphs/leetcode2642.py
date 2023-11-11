import heapq


class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self.adj = [[] for _ in range(n)]
        for src, dest, wt in edges:
            self.adj[src].append((wt, dest))

    def addEdge(self, edge: list[int]) -> None:
        node1, node2, weight = edge
        self.adj[node1].append([weight, node2])

    def shortestPath(self, node1: int, node2: int) -> int:
        minHeap = [[0, node1]]
        n = len(self.adj)
        costs = [float("inf") for _ in range(n)]
        costs[node1] = 0
        while len(minHeap) > 0:
            cost, node = heapq.heappop(minHeap)
            if cost > costs[node]:
                continue
            if node == node2:
                return cost
            for wt, dest in self.adj[node]:
                newWeight = wt + cost
                if newWeight < costs[dest]:
                    costs[dest] = newWeight
                    heapq.heappush(minHeap, [newWeight, dest])

        return -1


g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
print(g.shortestPath(3, 2))
print(g.shortestPath(0, 3))
g.addEdge([1, 3, 4])
print(g.shortestPath(0, 3))
