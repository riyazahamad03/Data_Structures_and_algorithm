import heapq


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        min_heap = [(n, idx) for idx, n in enumerate(nums)]
        heapq.heapify(min_heap)
        res = nums[::]
        while k > 0:
            min_val, idx = heapq.heappop(min_heap)
            new_val = min_val * multiplier
            res[idx] = new_val
            heapq.heappush(min_heap, (new_val, idx))
            k -= 1
        return res


x = Solution()
print(x.getFinalState(nums=[2, 1, 3, 5, 6], k=5, multiplier=2))
