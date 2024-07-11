class Solution:
    def reverseParentheses(self, s: str) -> str:
        st1, st2 = [], []

        for i in s:
            if i == ")":
                while st1:
                    val = st1.pop()
                    if val == "(":
                        break
                    st2.append(val)
                for k in st2:
                    # val = st2.pop()
                    st1.append(k)
                st2 = []
            else:
                st1.append(i)
        return "".join(st1)


x = Solution()
print(x.reverseParentheses(s="(u(love)i)"))
