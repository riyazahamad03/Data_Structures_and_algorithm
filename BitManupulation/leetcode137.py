class solution:
    def singleNumber(self, nums: list[int]):
        ones = twos = 0
        for n in nums:
            ones = (ones ^ n) & (~twos)
            twos = (twos ^ n) & (~ones)
        return ones


x = solution()
print(x.singleNumber([2, 2, 3, 2]))
