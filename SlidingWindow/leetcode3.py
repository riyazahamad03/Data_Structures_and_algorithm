'''

3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 

substring without repeating characters.

Input: s = "abcabcbb"

Output: 3

'''

class solution:
    def lengthOfLongestSubstring(self,s:str):
        l,res = 0,0
        Set = set()
        for r in range(len(s)):
            while s[r] in Set:
                Set.remove(s[l])
                l+=1
            Set.add(s[r])
            res = max(res, r-l+1)
        return res

x = solution()
print(x.lengthOfLongestSubstring('pwwkew'))