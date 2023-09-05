class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        l, r = 0, 1
        res, prev = 1, ""
        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            if arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""
        return res


x = Solution()
print(x.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
