class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        pali = []

        def dfs(idx):
            if idx >= len(s):
                res.append(pali.copy())
                return
            for j in range(idx, len(s)):
                if self.isPali(s, idx, j):
                    pali.append(s[idx : j + 1])
                    dfs(j + 1)
                    pali.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


x = Solution()
print(x.partition(s="aab"))
