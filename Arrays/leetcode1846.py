class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        arr.sort()
        arr[0] = 1
        for idx in range(1, len(arr)):
            if abs(arr[idx] - arr[idx - 1]) <= 1:
                continue
            arr[idx] = arr[idx - 1] + 1
        return arr[len(arr) - 1]


x = Solution()
print(x.maximumElementAfterDecrementingAndRearranging([2, 2, 1, 2, 1]))
