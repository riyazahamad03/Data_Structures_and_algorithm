class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()

        result = 0
        for i in range(len(seats)):
            result += abs(seats[i] - students[i])
        return result


x = Solution()
print(x.minMovesToSeat(seats=[3, 1, 5], students=[2, 7, 4]))
