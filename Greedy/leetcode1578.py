class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        l, res = 0, 0
        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    res += neededTime[l]
                    l = r
                else:
                    res += neededTime[r]
            else:
                l = r
        return res


x = Solution()
print(x.minCost("abaac", [1, 2, 3, 4, 5]))
