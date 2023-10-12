# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        mountain_arr = MountainArray(mountain_arr)
        length = mountain_arr.length()
        l, r = 1, length - 2
        while l <= r:
            m = (l + r)//2
            prev, curr, after = mountain_arr.get(
                m - 1), mountain_arr.get(m), mountain_arr.get(m + 1)
            if prev < curr < after:
                l = m + 1
            elif prev > curr > after:
                r = m - 1
            else:
                break

        peak = m
        l, r = 0, peak
        while l <= r:
            m = (l + r)//2
            v = mountain_arr.get(m)
            if v < target:
                l = m + 1
            elif v > target:
                r = m - 1
            else:
                return m

        l, r = peak, length - 1
        while l <= r:
            m = (l + r)//2
            v = mountain_arr.get(m)
            if v > target:
                l = m + 1
            elif v < target:
                r = m - 1
            else:
                return m
        return -1


x = Solution()
print(x.findInMountainArray(mountain_arr=[1, 2, 3, 4, 5, 3, 1], target=3))
