class Solution:
    def reverseWords(self, s: str) -> str:
        curr = []
        s = s + " "

        def rev(arrString):
            l, r = 0, len(arrString) - 1
            while l < r:
                arrString[l], arrString[r] = arrString[r], arrString[l]
                l, r = l + 1, r - 1
            return arrString
        res = []
        for r in range(len(s)):
            if s[r] == " ":

                res.append("".join(rev(curr)))
                curr = []

            else:
                curr.append(s[r])
        return " ".join(res)


x = Solution()
print(x.reverseWords(s="Let's take LeetCode contest"))
