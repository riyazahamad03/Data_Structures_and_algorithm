class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        res = []
        idx, jdx = 0, 0
        while idx < len(target):
            while jdx < target[idx] - 1:
                res.append("Push")
                res.append("Pop")
                jdx += 1
            res.append("Push")
            jdx = target[idx]
            idx += 1
        return res


x = Solution()
print(x.buildArray(target=[1, 3], n=3))
