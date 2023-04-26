import heapq
class solution:
    def lastStoneWeight(self , stones : list[int]):
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            fMax = heapq.heappop(stones)
            sMax = heapq.heappop(stones)
            if fMax != sMax:
                heapq.heappush(stones , fMax - sMax)
        stones.append(0)
        return abs(stones[0])
x = solution()
print(x.lastStoneWeight([2,7,4,1,8,1]))