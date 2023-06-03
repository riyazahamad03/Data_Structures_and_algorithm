import collections


class solution:
    def numOfminutes(self, n: int, headID: int, manager: list[int], informTime: list[int]):
        adj = collections.defaultdict(list)
        for i in range(n):
            adj[manager[i]].append(i)
        q = collections.deque()
        q.append((headID, 0))
        res = 0
        while q:
            head, totTime = q.popleft()
            res = max(res, totTime)
            for emp in adj[head]:
                q.append((emp, totTime + informTime[head]))

        return res


x = solution()
print(x.numOfminutes(n=6, headID=2, manager=[
      2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0]))
