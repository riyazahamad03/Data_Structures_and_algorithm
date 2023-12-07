class Solution:
    def largestOddNumber(self, num: str) -> str:
        # res = ""
        # val = ""
        # for n in range(len(num)):
        #     val += num[n]
        #     if int(num[n])%2:
        #         res = val

        # return res

        for i in range(len(num) - 1, -1, -1):
            if num[i] in ["1", "3", "5", "7", "9"]:
                return num[0 : i + 1]
        return ""


x = Solution()
print(x.largestOddNumber("35427"))
