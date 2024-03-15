class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pref = 1
        pre_array = [0] * (len(nums))
        for n in range(len(nums)):
            pre_array[n] = pref
            pref = pref * nums[n]

        post = 1
        post_array = [0] * (len(nums))
        for n in range(len(nums) - 1, -1, -1):
            post_array[n] = post
            post = post * nums[n]
        print(pre_array, post_array)
        res = []
        for i in range(len(nums)):
            res.append(pre_array[i] * post_array[i])
        return res


x = Solution()
print(x.productExceptSelf([-1, 1, 0, -3, 3]))
