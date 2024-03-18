class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        res = 0
        thres = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= thres:
                thres = min(thres, points[i][1])
                continue

            res += 1
            thres = points[i][1]
        return res + 1


x = Solution()
print(x.findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]))
