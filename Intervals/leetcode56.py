class Solution:
    def mergeInterVals(self,intervals:list[list[int]]):
        res = []
        intervals.sort(key=lambda x: x[0])
        res.append(intervals[0])
        for startVal,endVal in intervals[1:]:
            lastVal = res[-1][1]
            if startVal <= lastVal:
                res[-1][1] = max(lastVal,endVal)
            else:
                res.append([startVal,endVal])
        return res

x = Solution()
print(x.mergeInterVals([[1,4],[4,5]]))