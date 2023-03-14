class solution:
    def partition(self , s : str):
        res = []
        p = []


        
        def dfs(idex):
            if idex >= len(s):
                res.append(p.copy())
                return
            for j in range(idex , len(s)):
                if self.isPalindrome(s , idex , j ):
                    p.append(s[idex : j + 1])
                    dfs(j + 1)
                    p.pop()
        dfs(0)
        return res

    def isPalindrome(self , s , i , j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
x = solution()
print(x.partition("aab"))
