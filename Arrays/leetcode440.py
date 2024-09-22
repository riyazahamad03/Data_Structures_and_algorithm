class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        i = 1

        def count(curr):
            res = 0
            nei = curr + 1
            while curr <= n:
                res += min(nei, n + 1) - curr
                curr *= 10
                nei *= 10
            return res

        while i < k:
            steps = count(curr)
            if i + steps <= k:
                curr = curr + 1
                i += steps
            else:
                curr *= 10
                i += 1
        return curr


x = Solution()
print(x.findKthNumber(n=13, k=2))
