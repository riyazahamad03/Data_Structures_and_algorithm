class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:

        def can_place(x):
            prev_pos = position[0]
            balls_placed = 1

            for i in range(1, len(position)):
                curr = position[i]
                if curr - prev_pos >= x:
                    balls_placed += 1
                    prev_pos = curr
                if balls_placed == m:
                    return True
            return False

        res = 0
        n = len(position)
        position.sort()

        low, high = 1, int(position[-1] / (m - 1.0)) + 1

        while low <= high:
            mid = low + (high - low) // 2
            if can_place(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res


x = Solution()
print(x.maxDistance(position=[5, 4, 3, 2, 1, 1000000000], m=2))
