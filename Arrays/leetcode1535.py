class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        # rounds = 0
        # q = deque()
        # for i in range(len(arr)):
        #     q.append([arr[i] , 0])
        # while q:
        #     first = q.popleft()
        #     second = q.popleft()

        #     if first[1] == k or second[1] == k:
        #         return first[0] if first[1] == k else second[0]

        #     if first[0] > second[0]:
        #         q.appendleft([first[0] , first[1] + 1])
        #         q.append(second)
        #     else:
        #         q.appendleft([second[0] , second[1] + 1])
        #         q.append(first)
        #     rounds += 1

        currWinner = arr[0]
        wins = 0

        for i in range(1, len(arr)):
            if arr[i] > currWinner:
                wins = 1
                currWinner = arr[i]
            else:
                wins += 1

            if wins == k:
                return currWinner
        return currWinner


x = Solution()
print(x.getWinner(arr=[2, 1, 3, 5, 4, 6, 7], k=2))
