'''
leetcode : 271. Encode and Decode Strings
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

'''

class Solution:
    
    def encode(self,strs):
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res
    
    def decode(self,Str):
        res,p1 = [],0
        while p1 < len(Str):
            p2 = p1
            while Str[p2] != "#":
                p2+=1
            l = int(Str[p1:p2])
            res.append(Str[p2+1 : p2+1+l])
            p1 = p2+l+1
        return res
    
    def CheckValid(self,input,decoded):
        if input == decoded:
            return True
        else:
            return False

X = Solution()
strs = ["lint","code","love","you"]
encoded = X.encode(strs)
decoded = X.decode(encoded)

print(X.CheckValid(strs,decoded))



