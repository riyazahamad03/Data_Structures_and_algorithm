from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque, max_deque = deque(), deque()
        l = 0
        res = 0

        for r in range(len(nums)):
            # Maintain the min_deque
            while min_deque and nums[r] < nums[min_deque[-1]]:
                min_deque.pop()
            min_deque.append(r)

            # Maintain the max_deque
            while max_deque and nums[r] > nums[max_deque[-1]]:
                max_deque.pop()
            max_deque.append(r)

            # Ensure the difference between the max and min in the current window does not exceed the limit
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                l += 1
                if min_deque[0] < l:
                    min_deque.popleft()
                if max_deque[0] < l:
                    max_deque.popleft()

            res = max(res, r - l + 1)

        return res


x = Solution()
print(x.longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5))
