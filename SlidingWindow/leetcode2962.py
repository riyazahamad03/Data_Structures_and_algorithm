class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxNum = max(nums)
        cnt = [0] * (n + 1)
        maxCnt = 0
        for e in range(1, n + 1):
            if nums[e - 1] == maxNum:
                maxCnt += 1

            cnt[e] = maxCnt
        res = 0

        l, r = 1, 0
        while r <= n:
            while l < n and cnt[r] - cnt[l - 1] >= k:
                res += n - r + 1
                l += 1

            r += 1
        return res


x = Solution()
print(x.countSubarrays(nums=[1, 3, 2, 3, 3], k=2))
