class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        dp = {}  # [len , count]
        LenLis, res = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            maxLen, maxCnt = 1, 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    length, cnt = dp[j]
                    if length + 1 > maxLen:
                        maxLen, maxCnt = length + 1, cnt
                    elif length + 1 == maxLen:
                        maxCnt += cnt
            if maxLen > LenLis:
                LenLis, res = maxLen, maxCnt
            elif maxLen == LenLis:
                res += maxCnt
            dp[i] = [maxLen, maxCnt]
        return res


x = Solution()
print(x.findNumberOfLIS([1, 3, 5, 4, 7]))
