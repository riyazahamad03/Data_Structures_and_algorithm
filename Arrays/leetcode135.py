class Solution:
    def candy(self, ratings: list[int]) -> int:
        left = [1] * len(ratings)
        right = [1] * len(ratings)
        n = len(ratings)
        # Filling prefix
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] += left[i - 1]

        # filling postfix
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] += right[i + 1]

        res = 0
        for i in range(n):
            res += max(left[i], right[i])
        return res


x = Solution()
print(x.candy([1, 0, 2]))
