from collections import deque


class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        q = deque([i for i in range(len(tickets))])

        time = 0
        while q:
            time += 1
            front_person = q.popleft()
            tickets[front_person] -= 1
            if k == front_person and tickets[front_person] == 0:
                return time
            if tickets[front_person] != 0:
                q.append(front_person)
        return time


x = Solution()
print(x.timeRequiredToBuy(tickets=[2, 3, 2], k=2))
