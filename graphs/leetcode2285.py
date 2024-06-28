class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        arr = [0] * (n)
        for e1, e2 in roads:
            arr[e1] += 1
            arr[e2] += 1

        res = 0
        label = 1
        for n in sorted(arr):
            res += label * n
            label += 1
        return res


x = Solution()
print(x.maximumImportance(n=5, roads=[[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]))
