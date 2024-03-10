from collections import Counter

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        nums1 = Counter(nums1)
        nums2 = Counter(nums2)

        for n in nums1:
            if n in nums2:
                res.append(n)
        return res


x = Solution()
print(x.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
