import math


class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        minuteReach = []
        for d, s in zip(dist, speed):
            minuteReach.append(math.ceil(d / s))
        minuteReach.sort()
        res = 0
        for minute in range(len(minuteReach)):
            if minute >= minuteReach[minute]:
                return res
            res += 1
        return res


x = Solution()
print(x.eliminateMaximum(dist=[1, 3, 4], speed=[1, 1, 1]))
