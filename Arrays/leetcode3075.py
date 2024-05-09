class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)
        t = 0
        res = 0
        i = 0
        while k > 0:
            if happiness[i] - t <= 0:
                return res

            res += happiness[i] - t
            t += 1

            i += 1
            k -= 1
        return res


x = Solution()
print(x.maximumHappinessSum(happiness=[1, 2, 3], k=2))
