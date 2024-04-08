from collections import deque
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentQueue = deque(students)
        sandwichesQueue = deque(sandwiches)
        mp = {0: 0, 1: 0}
        for i in students:
            mp[i] += 1
        while sandwichesQueue and mp[sandwichesQueue[0]] > 0:
            val = studentQueue.popleft()
            if val == sandwichesQueue[0]:
                sandwichesQueue.popleft()
                mp[val] -= 1

            else:
                studentQueue.append(val)
        return len(studentQueue)


x = Solution()
print(x.countStudents(students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]))
