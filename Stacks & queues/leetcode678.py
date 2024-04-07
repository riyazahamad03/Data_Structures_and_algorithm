class Solution:
    def checkValidString(self, s: str) -> bool:
        st = []
        star = []
        for i in range(len(s)):
            if s[i] == "*":
                star.append(i)
            if s[i] == "(":
                st.append(i)
            elif s[i] == ")":
                if st:
                    st.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while star and st:
            if st.pop() > star.pop():
                return False
        return not st


x = Solution()
print(
    x.checkValidString(
        "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
    )
)
