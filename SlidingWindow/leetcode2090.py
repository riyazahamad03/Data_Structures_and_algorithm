class solution:
    def getAverages(self , nums : list[int] , k : int):
        res = [-1] * len(nums)
        d = 2 * k + 1
        l , window = 0 , 0
        for r in range(len(nums)):
            window += nums[r]
            if r - l + 1 == d:
                res[l + k] = window//d
                window -= nums[l]
                l += 1
        return res
x = solution()
print(x.getAverages(nums = [7,4,3,9,1,8,5,2,6], k = 3))
