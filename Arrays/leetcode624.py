class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]

        max_dist = 0

        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]

            max_dist = max(
                max_dist, abs(max_val - current_min), abs(current_max - min_val)
            )

            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)

        return max_dist


x = Solution()
print(x.maxDistance(arrays=[[1, 2, 3], [4, 5], [1, 2, 3]]))
