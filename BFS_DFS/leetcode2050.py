import collections


class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        # relations.sort(key = lambda x : x[1])
        adj = collections.defaultdict(list)
        inDeg = [0] * (n)
        for n1, n2 in relations:
            adj[n1 - 1].append(n2 - 1)
            inDeg[n2 - 1] += 1

        q = collections.deque()
        maxTime = [0] * (n)
        for i in range(n):
            if inDeg[i] == 0:
                maxTime[i] = time[i]
                q.append(i)
        while q:
            node = q.popleft()
            for nei in adj[node]:
                maxTime[nei] = max(maxTime[nei], maxTime[node] + time[nei])
                inDeg[nei] -= 1
                if inDeg[nei] == 0:
                    q.append(nei)
        return max(maxTime)


x = Solution()
print(x.minimumTime(n=3, relations=[[1, 3], [2, 3]], time=[3, 2, 5]))
