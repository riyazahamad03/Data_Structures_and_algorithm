class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        tmpHeight = heights.copy()
        tmpHeight.sort()
        res = 0
        for i in range(len(tmpHeight)):
            if tmpHeight[i] != heights[i]:
                res += 1
        return res


x = Solution()
print(x.heightChecker(heights=[1, 1, 4, 2, 1, 3]))
