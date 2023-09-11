class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        res = []
        hashMap = {i: [] for i in groupSizes}
        for i in range(len(groupSizes)):
            hashMap[groupSizes[i]].append(i)
        for i in hashMap:
            for j in range(0, len(hashMap[i]), i):
                res.append(hashMap[i][j: j + i])
        return res


x = Solution()
print(x.groupThePeople(groupSizes=[3, 3, 3, 3, 3, 1, 3]))
