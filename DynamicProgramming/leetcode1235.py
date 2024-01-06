import bisect


class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        intervals = sorted(zip(startTime, endTime, profit))

        def binSearch(low, high, tar):
            res = -1
            while low <= high:
                mid = (low + high) // 2
                mid_val = intervals[mid][0]

                if mid_val < tar:
                    low = mid + 1
                elif mid_val >= tar:
                    res = mid
                    high = mid - 1

            return res

        dp = {}

        def dfs(i):
            if i == len(intervals):
                return 0
            if i in dp:
                return dp[i]

            res = dfs(i + 1)
            # idx = binSearch(i + 1 , len(intervals) - 1 , intervals[i][1])
            idx = bisect.bisect(intervals, (intervals[i][1], -1, -1))

            if idx != -1:
                res = max(res, intervals[i][2] + dfs(idx))
            dp[i] = res
            return res

        return dfs(0)


x = Solution()
print(x.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
