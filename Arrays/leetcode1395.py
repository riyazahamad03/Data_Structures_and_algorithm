class Solution:
    def numTeams(self, rating: list[int]) -> int:
        res = 0

        for i in range(len(rating)):
            left_smaller, right_larger = 0, 0

            curr = rating[i]

            for j in range(i):
                if curr > rating[j]:
                    left_smaller += 1

            for j in range(i + 1, len(rating)):
                if curr < rating[j]:
                    right_larger += 1

            res += left_smaller * right_larger

            left_larger = i - left_smaller
            right_smaller = len(rating) - i - 1 - right_larger
            res += left_larger * right_smaller
        return res


x = Solution()
print(x.numTeams([2, 5, 3, 4, 1]))
