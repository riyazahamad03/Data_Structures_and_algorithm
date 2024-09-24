from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = {}

        for num in arr1:
            str_num = str(num)
            for i in range(1, len(str_num) + 1):
                prefix = str_num[:i]
                prefixes[prefix] = prefixes.get(prefix, 0) + 1

        max_len = 0

        for num in arr2:
            str_num = str(num)
            for i in range(1, len(str_num) + 1):
                prefix = str_num[:i]
                if prefix in prefixes:
                    max_len = max(max_len, i)
                else:
                    break

        return max_len


x = Solution()
print(x.longestCommonPrefix(arr1=[1, 10, 100], arr2=[1000]))
