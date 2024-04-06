class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        cnt = 0
        st = []

        for i in s:
            if i == "(":
                cnt += 1
                st.append(i)
            elif i == ")" and cnt > 0:
                cnt -= 1
                st.append(i)
            elif i != ")":
                st.append(i)
        fil = []
        for i in st[::-1]:
            if i == "(" and cnt > 0:
                cnt -= 1
            else:
                fil.append(i)
        return "".join(fil[::-1])


x = Solution()
print(x.minRemoveToMakeValid(s="lee(t(c)o)de)"))
