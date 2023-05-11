class solution:
    def maxUncrossedLinesUsingRecurrsion(self, nums1: list[int], nums2: list[int]):
        def dfs(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            if nums1[i] == nums2[j]:
                return 1 + dfs(i + 1, j + 1)
            else:
                return max(dfs(i + 1, j), dfs(i, j + 1))
        return dfs(0, 0)

    def maxUncrossedLinesUsingRecurrsionAndMemoization(self, nums1: list[int], nums2: list[int]):
        dp = {}

        def dfs(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if nums1[i] == nums2[j]:
                dp[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return dp[(i, j)]
        return dfs(0, 0)

    def maxUncrossedLinesUsingTrueDp(self, nums1: list[int], nums2: list[int]):
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1) - 1, - 1, - 1):
            for j in range(len(nums1) - 1, - 1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]


x = solution()
# timeComplexity = O(2 ^ m + n)
print(x.maxUncrossedLinesUsingRecurrsion([1, 4, 2], [1, 2, 4]))
# timeComplexity = O(m * n)
print(x.maxUncrossedLinesUsingRecurrsionAndMemoization([1, 4, 2], [1, 2, 4]))
# timeComplexity = O(m * n)
print(x.maxUncrossedLinesUsingTrueDp([1, 4, 2], [1, 2, 4]))
