class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        xrep, yrep = 0, 0
        xSum, ySum = 0, 0

        for i in nums1:
            if i == 0:
                xrep += 1
            xSum += i

        for i in nums2:
            if i == 0:
                yrep += 1
            ySum += i

        if xrep == 0 and yrep == 0:
            return -1 if xSum != ySum else xSum
        if xrep == 0:
            return xSum if yrep + ySum <= xSum else -1
        if yrep == 0:
            return ySum if xrep + xSum <= ySum else -1

        return max(xSum + xrep, ySum + yrep)


x = Solution()
print(x.minSum(nums1=[3, 2, 0, 1, 0], nums2=[6, 5, 0]))
