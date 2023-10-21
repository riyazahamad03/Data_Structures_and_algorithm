import heapq


class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        # cache = {}
        # def dfs(i , prev):
        #     if i >= len(nums):
        #         return 0
        #     if (i , prev) in cache:
        #         return cache[(i , prev)]
        #     res = 0
        #     if i - prev <= k:
        #         res = max(nums[i] + dfs(i + 1 , i) , dfs(i + 1 , prev))
        #     else:
        #         res = dfs(i + 1 , prev)

        #     cache[(i , prev)] = res
        #     return res
        # return dfs(0 , 0) if dfs(0 , 0) != 0 else max(nums)

        # dp = [0] * (len(nums))
        # for i in range(len(nums) - 1 , - 1 , - 1):
        #     dp[i] = nums[i]
        #     for j in range(i + 1  , len(nums)):
        #         if j - i > k:
        #             break
        #         dp[i] = max(dp[i] , nums[i] + dp[j])
        # return max(dp)

        maxHeap = [[-1 * nums[0], 0]]
        res = nums[0]
        for i in range(1, len(nums)):
            while i - maxHeap[0][1] > k:
                heapq.heappop(maxHeap)
            val = nums[i] + max(0, -1 * maxHeap[0][0])
            res = max(res, val)
            heapq.heappush(maxHeap, [-1 * val, i])
        return res


x = Solution()
print(x.constrainedSubsetSum(nums=[10, -2, -10, -5, 20], k=2))
