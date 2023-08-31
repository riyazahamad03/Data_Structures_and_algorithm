class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        maxReach = [0] * (n + 1)
        for i in range(len(ranges)):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])

            maxReach[left] = max(maxReach[left], right)

        taps, curr, nxt = 0, 0, 0
        for i in range(n + 1):
            if i > nxt:
                return -1
            if i > curr:
                taps += 1
                curr = nxt
            nxt = max(nxt, maxReach[i])
        return taps


x = Solution()
print(x.minTaps(n=5, ranges=[3, 4, 1, 1, 0, 0]))
