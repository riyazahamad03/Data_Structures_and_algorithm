import collections


class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        d = collections.defaultdict(list)

        def getCount(x):
            cnt = 0
            while x > 0:
                if x & 1:
                    cnt += 1
                x >>= 1
            return cnt

        res = []
        for i in range(len(arr)):
            d[getCount(arr[i])].append(arr[i])
        for i in sorted(d.keys()):
            res += list(sorted(d[i]))
        return res


x = Solution()
print(x.sortByBits(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8]))
