class Solution:
    def minOperations(self, logs: list[str]) -> int:
        res = 0
        logSet = set()
        for log in logs:
            if log == "../":
                res = max(res - 1, 0)
            elif log != "./":
                # val = log.split('/')[0]
                # logSet.add(val)
                res += 1
        return res


x = Solution()
print(x.minOperations(logs=["d1/", "d2/", "../", "d21/", "./"]))
