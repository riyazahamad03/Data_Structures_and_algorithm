class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        m = len(rolls)
        total_sum = mean * (m + n)
        missing_sum = total_sum - sum(rolls)

        if missing_sum > 6 * n or missing_sum < n:
            return []
        res = []

        while n:
            dice = min(6, missing_sum - n + 1)
            res.append(dice)
            missing_sum -= dice
            n -= 1
        return res


x = Solution()
print(x.missingRolls(rolls=[3, 2, 4, 3], mean=4, n=2))
