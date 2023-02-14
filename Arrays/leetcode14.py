class solution:
    def longestCommonPrefix(self,strs:list[str]):
        res = ""
        for i in range(len(strs[0])):
            pref = strs[0][i]
            for j in range(1,len(strs)):
                if i == len(strs[j]) or pref != strs[j][i]:
                    return res
            res += pref
        return res
x = solution()
print(x.longestCommonPrefix(["flower","flow","flight"]))
