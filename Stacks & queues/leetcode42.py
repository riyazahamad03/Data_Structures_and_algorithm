class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_maximum, right_maximum = height[0], height[right]
        res = 0
        while left < right:
            if left_maximum < right_maximum:
                left += 1
                left_maximum = max(left_maximum, height[left])
                res += left_maximum - height[left]

            else:
                right -= 1
                right_maximum = max(height[right], right_maximum)
                res += right_maximum - height[right]

        return res


x = Solution()
print(x.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
