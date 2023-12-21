class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points.sort()
        prev = points[0][0]
        res = 0
        for x1, y1 in points[1::]:
            res = max(res, x1 - prev)
            prev = x1
        return res


x = Solution()
print(x.maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]))
