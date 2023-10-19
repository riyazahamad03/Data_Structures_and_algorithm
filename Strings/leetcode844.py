class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1 , st2 = [] , []

        for i in range(len(s)):
            if s[i] == "#":
                if st1:
                    st1.pop()
            else:
                st1.append(s[i])
        
        for i in range(len(t)):
            if t[i] == "#":
                if st2:
                    st2.pop()
            else:
                st2.append(t[i])

        return st1 == st2

x = Solution()
print(x.backspaceCompare('s#s#' , 'p#p#'))