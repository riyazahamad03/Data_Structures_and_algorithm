import collections


class solution:
    def isBipartite(self, graph: list[list[int]]):
        odd = [0] * len(graph)

        def bfs(node):
            if odd[node]:
                return True
            q = collections.deque([node])
            odd[node] = - 1
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if odd[node] == odd[nei]:
                        return False
                    elif not odd[nei]:
                        q.append(node)
                        odd[nei] = - 1 * odd[node]
            return True
        for node in range(len(graph)):
            if not bfs(node):
                return False
        return True


x = solution()
print(x.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
