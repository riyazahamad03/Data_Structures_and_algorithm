import collections


class Solution:
    def numBusesToDestination(
        self, routes: list[list[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        adj = collections.defaultdict(list)

        for i, elems in enumerate(routes):
            for node in elems:
                adj[node].append(i)
        q = collections.deque()

        visited = set()
        for route in adj[source]:
            q.append(route)
            visited.add(route)

        bus = 1
        while q:
            for idx in range(len(q)):
                node = q.popleft()
                for route in routes[node]:
                    if route == target:
                        return bus
                    for nxt in adj[route]:
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append(nxt)
            bus += 1
        return -1


x = Solution()
print(x.numBusesToDestination(routes=[[1, 2, 7], [3, 6, 7]], source=1, target=6))
