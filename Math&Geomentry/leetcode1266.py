class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        res = 0
        prevP1, prevP2 = points[0]
        for p1, p2 in points[1::]:
            res += max(abs(p1 - prevP1), abs(p2 - prevP2))
            prevP1, prevP2 = p1, p2
        return res


x = Solution()
print(x.minTimeToVisitAllPoints(points=[[1, 1], [3, 4], [-1, 0]]))
