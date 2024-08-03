from collections import Counter
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        c1 = Counter(target)
        c2 = Counter(arr)

        if len(c1) != len(c2):
            return False
        for n in c1:
            if n not in c2 or c1[n] != c2[n]:
                return False
        return True


x = Solution()
print(x.canBeEqual(target=[1, 2, 3, 4], arr=[2, 4, 1, 3]))
