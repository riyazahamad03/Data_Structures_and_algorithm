class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for i in range(len(s)):
            curr = ord(s[i])
            if st and abs(ord(st[-1]) - curr) == 32:
                st.pop()
            else:
                st.append(s[i])
        return "".join(st)


x = Solution()
print(x.makeGood(s="leEeetcode"))
