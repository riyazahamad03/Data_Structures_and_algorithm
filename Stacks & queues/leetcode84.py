class solution:
    def largestRectangle(self, heights: list[int]):
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            startIndex = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))

                startIndex = idx
            stack.append((startIndex, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea


x = solution()
print(x.largestRectangle([2, 1, 5, 6, 2, 3]))
print(x.largestRectangle([2, 4]))
