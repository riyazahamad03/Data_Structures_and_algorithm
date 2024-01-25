class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        if len(s) > 12:
            return res

        def dfs(i, dot, currIp):
            if dot == 4 and i == len(s):
                res.append(currIp[:-1])
                return

            if dot > 4:
                return

            for j in range(i, min(i + 3, len(s))):
                if int(s[i : j + 1]) < 256 and (i == j or s[i] != "0"):
                    dfs(j + 1, dot + 1, currIp + s[i : j + 1] + ".")

        dfs(0, 0, "")
        return res


x = Solution()
print(x.restoreIpAddresses(s="25525511135"))
