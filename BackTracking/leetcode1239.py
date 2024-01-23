class Solution:
    def maxLength(self, arr: list[str]) -> int:
        chSet = set()

        def overLapping(s):
            prev = set()
            for c in s:
                if c in prev or c in chSet:
                    return True
                prev.add(c)
            return False

        def dfs(i):
            if i == len(arr):
                return len(chSet)
            res = 0

            if not overLapping(arr[i]):
                for c in arr[i]:
                    chSet.add(c)
                res = dfs(i + 1)

                for c in arr[i]:
                    chSet.remove(c)
            return max(res, dfs(i + 1))

        return dfs(0)


x = Solution()
print(x.maxLength(arr=["un", "iq", "ue"]))
