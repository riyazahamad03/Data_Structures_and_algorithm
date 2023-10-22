class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        # res = float("-inf")
        # for i in range(len(nums)):
        #     for j in range(i + 1 , len(nums)):
        #         if j - i + 1 > k:
        #             res = max(res , min(nums[i : j + 1]) * (j - i + 1))
        # return res
        n = len(nums)
        left = [-1] * (n)
        stack = []
        for i in range(n - 1, - 1, - 1):
            while stack and nums[stack[-1]] > nums[i]:
                left[stack.pop()] = i
            stack.append(i)

        right = [n] * (n)
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                right[stack.pop()] = i
                print(right)
            stack.append(i)
        res = 0
        for i in range(n):
            if left[i] < k and right[i] > k:
                res = max(res, nums[i] * (right[i] - left[i] - 1))
        print(left, right)
        return res


x = Solution()
print(x.maximumScore(nums=[1, 4, 3, 7, 4, 5], k=3))
