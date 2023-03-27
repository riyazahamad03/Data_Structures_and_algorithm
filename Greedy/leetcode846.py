import heapq
class solution:
    def isNStraightHand(self, hand:list[list[int]] , groupSize : int):
        if len(hand)%groupSize:
            return False
        counter = {}
        for num in hand:
            counter[num] = 1 + counter.get(num , 0)
        minHeap = list(counter.keys()) 
        heapq.heapify(minHeap)

        while minHeap:
            topElem = minHeap[0]
            for idex in range(topElem , topElem + groupSize):
                if idex not in counter:
                    return False
                counter[idex] -= 1
                if counter[idex] == 0:
                    if idex != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
x = solution()
print(x.isNStraightHand([1,2,3,6,2,3,4,7,8] , 3))