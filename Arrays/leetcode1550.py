class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        for i in range(len(arr) - 2):
            if arr[i] % 2 == arr[i + 1] % 2 == arr[i + 2] % 2 == 1:
                return True
        return False


x = Solution()
print(x.threeConsecutiveOdds(arr=[1, 2, 34, 3, 4, 5, 7, 23, 12]))
