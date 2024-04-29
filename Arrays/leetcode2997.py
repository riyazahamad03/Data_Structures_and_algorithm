class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0

        for bit_position in range(31, -1, -1):
            mask = 1 << bit_position
            count_set_bits = 0

            for num in nums:
                if num & mask:
                    count_set_bits += 1

            if count_set_bits % 2 != (k & mask) >> bit_position:
                ans += 1

        return ans


z = Solution()
print(z.minOperations(nums=[2, 1, 3, 4], k=1))
