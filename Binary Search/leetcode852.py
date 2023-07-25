class solution:
    def peakIndexInMountain(self, arr: list[int]):
        l, r = 0, len(arr)
        while l < r:
            m = (l + r)//2
            if arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m - 1
        return l , arr[l]


x = solution()
print(x.peakIndexInMountain(arr=[0, 10, 5, 2]))
