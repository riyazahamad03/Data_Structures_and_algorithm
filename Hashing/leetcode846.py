import heapq


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        counter = {}
        for num in hand:
            counter[num] = 1 + counter.get(num, 0)
        minH = list(counter.keys())
        heapq.heapify(minH)
        while minH:
            top = minH[0]
            for idex in range(top, top + groupSize):
                if idex not in counter:
                    return False
                counter[idex] -= 1
                if counter[idex] == 0:
                    if idex != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True


x = Solution()
print(x.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3))
