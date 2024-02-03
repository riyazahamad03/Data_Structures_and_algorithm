from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = {}

        def dfs(idx):
            if idx == len(arr):
                return 0
            if idx in cache:
                return cache[idx]
            max_partition_sum = float("-inf")
            l = 0
            maxi = float("-inf")
            for i in range(idx, min(idx + k, len(arr))):
                l += 1
                maxi = max(maxi, arr[i])
                s = (l * max(arr[idx : i + 1])) + dfs(i + 1)
                max_partition_sum = max(max_partition_sum, s)
            cache[idx] = max_partition_sum
            return max_partition_sum

        return dfs(0)
x = Solution()
print(x.maxSumAfterPartitioning([1,15,7,9,2,5,10] , 3))