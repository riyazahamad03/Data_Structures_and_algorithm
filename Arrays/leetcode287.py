class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow, fast = 0, slow
        while True:
            slow = nums[slow]
            fast = nums[fast]

            if slow == fast:
                return slow


x = Solution()
print(x.findDuplicate([3, 3, 3, 3, 3]))
