import collections


class solution:
    def shortestPathToReach(self, graph: list[list[int]]):
        n = len(graph)
        q = collections.deque([(1 << i, i, 0)
                              for i in range(n)])  # (mask , node , cost)
        visited = set((1 << i, i) for i in range(n))  # (mask , node)

        # print(q, visited)
        while q:
            print(visited)

            if mask == (1 << n) - 1:
                return cost

            for nei in graph[node]:
                newMask = mask | (1 << nei)

                if (newMask, nei) not in visited:
                    q.append((newMask, nei, cost + 1))
                    visited.add((newMask, nei))
        return -1


x = solution()
print(x.shortestPathToReach([[1, 2], [0], [0]]))
