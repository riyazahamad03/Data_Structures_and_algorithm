import heapq
class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        # piles.sort(reverse=True)
        # res = 0
        # a, riyaz, b = 0, 1, len(piles) - 1

        # for i in range(len(piles) // 3):
        #     res += piles[riyaz]
        #     a = riyaz + 1
        #     riyaz = riyaz + 2
        #     b = b - 1
        # return res

        heap = []
        for i in range(len(piles)):
            heapq.heappush(heap, -1 * piles[i])
        res = 0
        for i in range(len(piles) // 3):
            heapq.heappop(heap)
            res += -1 * heapq.heappop(heap)
        return res


x = Solution()
print(x.maxCoins([2, 4, 1, 2, 7, 8]))
