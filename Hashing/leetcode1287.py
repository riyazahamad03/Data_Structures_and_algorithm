import collections


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        res = 0
        cnt = collections.defaultdict(int)
        tar = len(arr) / 4

        for num in arr:
            cnt[num] += 1

        for key, val in cnt.items():
            if val > tar:
                return key
        return -1


x = Solution()
print(x.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))
