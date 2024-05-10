import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        min_heap = []
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                val = arr[i] / arr[j]
                heapq.heappush(min_heap, [val, [arr[i], arr[j]]])
        while k > 1:
            heapq.heappop(min_heap)
            k -= 1
        val, res = heapq.heappop(min_heap)
        return res


x = Solution()
print(x.kthSmallestPrimeFraction(arr=[1, 2, 3, 5], k=3))
