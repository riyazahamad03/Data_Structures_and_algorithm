class solution:
    def permute(self, nums:list[int]):
        res = []

        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
                        
            res.extend(perms)
            # print(res , i )
            nums.append(n)
        return res
x = solution()
print(x.permute([1,2,3]))