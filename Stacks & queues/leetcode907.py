class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        mod = 10**9 + 7
        stack = []
        minSum = 0

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                m = stack.pop()
                lft = -1 if not stack else stack[-1]
                rgh = i

                cnt = (m - lft) * (rgh - m)
                minSum += cnt * arr[m]
            stack.append(i)
        return minSum % mod


x = Solution()
print(x.sumSubarrayMins([3, 1, 2, 4]))
