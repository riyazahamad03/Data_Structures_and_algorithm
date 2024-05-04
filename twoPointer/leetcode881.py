class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        res = 0
        while l <= r:
            remaining = limit - people[r]
            res += 1
            r -= 1
            if l <= r and remaining >= people[l]:
                l += 1
        return res


x = Solution()
print(x.numRescueBoats([3, 5, 3, 4], 5))
