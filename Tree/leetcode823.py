class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        mod = 10**9 + 7
        cntMap = {}
        for i in arr:
            cntMap[i] = 1

        n = len(arr)
        arr.sort()
        for i in range(n):
            cnt = 0
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    if arr[i] // arr[j] in cntMap:
                        left = cntMap[arr[j]]
                        right = cntMap[arr[i] / arr[j]]

                        cnt += left * right
            cntMap[arr[i]] += cnt
        return sum(cntMap.values()) % mod


x = Solution()
print(x.numFactoredBinaryTrees([2, 4, 5, 10]))
