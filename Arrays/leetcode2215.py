from collections import defaultdict


class solution:
    def findDifference(self, nums1: list[int], nums2: list[int]):
        d1, d2 = defaultdict(int), defaultdict(int)
        for i in nums1:
            d1[i] = 1
        for j in nums2:
            d2[j] = 1

        res = [[] for _ in range(2)]

        for idx in range(len(nums1)):
            if not d2[nums1[idx]]:
                res[0].append(nums1[idx])
                d2[nums1[idx]] = 1

        for jdx in range(len(nums2)):
            if not d1[nums2[jdx]]:
                res[1].append(nums2[jdx])
                d1[nums2[jdx]] = 1
        return res


x = solution()
print(x.findDifference([1, 2, 3], [2, 4, 6]))

# timeComplexity O(m + n)
#spaceComplexity O(m + n)