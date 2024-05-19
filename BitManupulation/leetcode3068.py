class Solution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        delta = [(n ^ k) - n for n in nums]
        delta.sort(reverse=True)
        res = sum(nums)
        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                break
            path = delta[i] + delta[i + 1]
            if path <= 0:
                break
            res += path
        return res


x = Solution()
print(
    x.maximumValueSum(
        nums=[7, 7, 7, 7, 7, 7], k=3, edges=[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
    )
)
