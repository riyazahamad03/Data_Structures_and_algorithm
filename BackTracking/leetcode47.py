class solution:
    def permUnique(self,nums:list[int]):
        result = []
        permutations = []
        c = { n : 0 for n in nums}

        for n in nums:
            c[n] += 1
        
        def dfs():
            if len(permutations) == len(nums):
                result.append(permutations.copy())
                return

            for n in c:
                if c[n] > 0:
                    permutations.append(n)
                    c[n] -= 1

                    dfs()

                    c[n] += 1
                    permutations.pop()
        dfs()
        return result
x=solution()
print(x.permUnique([1,1,2]))