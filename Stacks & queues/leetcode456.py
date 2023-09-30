class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        # n = len(nums)
        # q = deque()
        # for i in range(n - 2):
        #     q.append((nums[i] , i , 'U' , float("-inf")))

        # while q:
        #     elem , idx , p , prev = q.popleft()

        #     if p == 'U':
        #         for j in range(idx , n):
        #             if nums[j] > elem:
        #                 q.append((nums[j] , j , 'D' , elem))
        #     if p == 'D':
        #         for k in range(idx , n):
        #             if nums[k] < elem and nums[k] > prev:
        #                 return True
        # return False
        n = len(nums)
        stack = []
        currMin = float("inf")
        for n in nums:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n > stack[-1][1]:
                return True
            stack.append([n, currMin])
            currMin = min(currMin, n)
        return False


x = Solution()
print(x.find132pattern(nums=[1, 2, 3, 4]))
