class solution:
    def lengthOfLIS(self , nums:list[int]):
        Lis = [1] * len(nums)
        for i in range(len(nums)-1 , -1 ,-1):
            for j in range(i + 1 , len(nums)):
                if nums[i] < nums[j]:
                    Lis[i] = max(Lis[i] , 1 + Lis[j])
        return max(Lis)
x = solution()
print(x.lengthOfLIS([10,9,2,5,3,7,101,18]))