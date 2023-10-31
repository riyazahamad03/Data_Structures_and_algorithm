class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        xorVal = 0
        res = []

        for i in range(len(pref)):
            newVal = xorVal ^ pref[i]
            res.append(newVal)
            xorVal = xorVal ^ newVal
        return res
        
x = Solution()
print(x.findArray([5,2,0,3,1]))