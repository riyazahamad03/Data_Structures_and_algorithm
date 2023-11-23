class Solution:
    def checkArithmeticSubarrays(
        self, nums: list[int], l: list[int], r: list[int]
    ) -> list[bool]:
        def check(arr):
            arr.sort()
            diff = arr[1] - arr[0]

            for i in range(2, len(arr)):
                if arr[i] - arr[i - 1] != diff:
                    return False
            return True

        res = []

        for i in range(len(l)):
            arr = nums[l[i] : r[i] + 1]
            res.append(check(arr))
        return res


x = Solution()
print(x.checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]))
