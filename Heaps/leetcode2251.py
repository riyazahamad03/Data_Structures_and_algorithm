import heapq


class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        people = [(p, idx) for idx, p in enumerate(people)]
        start, end = [], []
        cnt = 0
        for f1, f2 in flowers:
            start.append(f1)
            end.append(f2)

        heapq.heapify(start)
        heapq.heapify(end)

        res = [0] * (len(people))
        for p, idx in sorted(people):
            while start and start[0] <= p:
                heapq.heappop(start)
                cnt += 1
            while end and end[0] < p:
                cnt -= 1
                heapq.heappop(end)
            res[idx] = cnt
        return res


x = Solution()
print(x.fullBloomFlowers([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11]))
