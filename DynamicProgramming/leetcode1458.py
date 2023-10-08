class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        dp = {}  # i , j

        def dfs(i, j, idx):
            if i == len(nums1) or j == len(nums2):
                return -1 if not idx else 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = nums1[i] * nums2[j] + dfs(i + 1, j + 1, 1)
            res1 = dfs(i + 1, j, idx)
            res2 = dfs(i, j + 1, idx)
            dp[(i, j)] = max(res1, res, res2)
            return dp[(i, j)]
        return dfs(0, 0, 1) if dfs(0, 0, 1) != 0 else max(sorted(nums1)[0] * sorted(nums2)[-1], sorted(nums2)[0] * sorted(nums1)[-1])


x = Solution()
print(x.maxDotProduct(nums1=[2, 1, -2, 5], nums2=[3, 0, -6]))
