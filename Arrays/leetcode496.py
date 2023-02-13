class solution:
    def nextGreaterElement(self,nums1:list[int],nums2:list[int]):
        
        numsIndex = {nums1[i] : i for i in range(len(nums1))}
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idex = numsIndex[val]
                res[idex] = curr
            if curr in nums1:
                stack.append(curr)
        return res

x = solution()
print(x.nextGreaterElement([2,4],[1,2,3,4]))

