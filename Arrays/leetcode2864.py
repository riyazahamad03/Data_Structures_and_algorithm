class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        arr = list(s)
        l = 0
        i = 0
        while i < len(arr):
            if arr[i] == "1":
                arr[i], arr[l] = arr[l], arr[i]
                l += 1
            i += 1
        arr[l - 1], arr[len(s) - 1] = arr[len(s) - 1], arr[l - 1]
        return "".join(arr)


x = Solution()
print(x.maximumOddBinaryNumber("0101"))
