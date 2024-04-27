class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = [0] * (len(ring))

        for k in range(len(key) - 1, -1, -1):
            next_dp = [float("inf")] * (len(ring))
            for r in range(len(ring)):
                for i, c in enumerate(ring):
                    if c == key[k]:
                        mini = min(abs(r - i), len(ring) - abs(r - i))
                        next_dp[r] = min(next_dp[r], mini + 1 + dp[i])
            dp = next_dp
        return dp[0]


x = Solution()
print(x.findRotateSteps(ring="godding", key="gd"))
