class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)

            if len(hashMap) <= 2:
                continue

            newMap = {}
            for n in hashMap:
                if hashMap[n] - 1 > 0:
                    newMap[n] = hashMap[n] - 1
            hashMap = newMap

        res = []
        for n in hashMap:
            if nums.count(n) > len(nums)//3:
                res.append(n)
        return res


x = Solution()
print(x.majorityElement([3, 2, 3]))
