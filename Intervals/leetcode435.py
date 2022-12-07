'''

435. Non-overlapping Intervals
Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

'''

class solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x : x[0])
        count = 0
        prevEnd = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            else:
                count+=1
                prevEnd = min(prevEnd,intervals[i][1])
        return count
x = solution()
print(x.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))