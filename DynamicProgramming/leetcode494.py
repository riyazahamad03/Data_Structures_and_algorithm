class solution:
    def targetSumWays(self, nums: list[int], target):
        dp = {} #for caching purpose
        def backTrack(idex, tot):
            if idex == len(nums):
                return 1 if target == tot else 0
            if (idex , tot) in dp:
                return dp[(idex,tot)]
            dp[(idex , tot)] = backTrack(idex + 1 , tot + nums[idex]) + backTrack(idex + 1 , tot-nums[idex])
            return dp[(idex , tot)]
        return backTrack(0 , 0)
x = solution()
print(x.targetSumWays([1,1,1,1,1] , 3))
