from typing import List
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        avail = [i for i in range(n)]
        used = []
        count = [0] * n

        for start, end in meetings:
            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(avail, room)

            if not avail:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(avail, room)
            room = heapq.heappop(avail)
            heapq.heappush(used, (end, room))
            count[room] += 1
        return count.index(max(count))


x = Solution()
print(x.mostBooked(n=2, meetings=[[0, 10], [1, 5], [2, 7], [3, 4]]))
