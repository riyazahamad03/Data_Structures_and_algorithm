import math


class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:

        def getHour(x):
            tot = 0
            for i in range(len(dist)):
                if i != len(dist) - 1:
                    val = dist[i]/x
                    tot += math.ceil(val)
                else:
                    tot += dist[i]/x
            return tot

        left, right = 1, 10000000
        minSpeed = -1
        while left <= right:
            mid = (left + right)//2
            if getHour(mid) <= hour:
                minSpeed = mid
                right = mid - 1
            else:
                left = mid + 1
        return minSpeed


x = Solution()
print(x.minSpeedOnTime(dist=[1, 3, 2], hour=6))
