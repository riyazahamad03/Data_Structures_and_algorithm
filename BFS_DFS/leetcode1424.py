import collections


class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        q = collections.deque([(0, 0)])
        res = []

        while q:
            row, col = q.popleft()
            res.append(nums[row][col])

            if col == 0 and row + 1 < len(nums):
                q.append((row + 1, col))
            if col + 1 < len(nums[row]):
                q.append((row, col + 1))
        return res


x = Solution()
print(x.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
