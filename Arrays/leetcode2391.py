class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        paperIdx, glassIdx, metalIdx = -1, -1, -1

        for i in range(len(garbage) - 1, -1, -1):
            if "P" in garbage[i] and not paperIdx != -1:
                paperIdx = i
            if "G" in garbage[i] and not glassIdx != -1:
                glassIdx = i
            if "M" in garbage[i] and not metalIdx != -1:
                metalIdx = i

        def getCount(garb, idx):
            res = 0
            res += garbage[0].count(garb)
            for i in range(1, len(garbage)):
                Count = garbage[i].count(garb)
                if i <= idx:
                    res += Count
                    res += travel[i - 1]
            return res

        return (
            getCount("G", glassIdx) + getCount("M", metalIdx) + getCount("P", paperIdx)
        )


x = Solution()
print(x.garbageCollection(garbage=["G", "P", "GP", "GG"], travel=[2, 4, 3]))
