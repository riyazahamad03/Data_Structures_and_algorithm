class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums)
        nums = set(nums)

        def gen(curr):
            if len(curr) == n:
                if curr not in nums:
                    return curr
                return ""
            add = gen(curr + "0")
            if add:
                return add
            return gen(curr + "1")

        return gen("")


x = Solution()
print(x.findDifferentBinaryString(nums=["01", "10"]))
