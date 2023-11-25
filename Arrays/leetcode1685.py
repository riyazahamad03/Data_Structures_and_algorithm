class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pref, post = [0] * (n), [0] * (n)

        cnt = 0
        for i in range(n):
            pref[i] += cnt
            cnt += nums[i]

        cnt = 0
        for i in range(n - 1, -1, -1):
            post[i] += cnt
            cnt += nums[i]
        print(pref, post)
        res = []

        for i in range(n):
            prev = (i * (nums[i])) - pref[i]
            nxt = post[i] - ((n - i - 1) * (nums[i]))
            res.append(nxt + prev)

        return res


x = Solution()
print(x.getSumAbsoluteDifferences([2, 3, 5]))
