import itertools


class solution:
    def maxAcheivable(self, n: int, requests: list[list[int]]):
        for k in range(len(requests), 0, -1):

            for c in itertools.combinations(range(len(requests)), k):
                deg = [0] * n

                for i in c:
                    deg[requests[i][0]] -= 1
                    deg[requests[i][1]] += 1

                if not any(deg):
                    return k
        return 0


x = solution()
print(x.maxAcheivable(n=5, requests=[
      [0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]))
