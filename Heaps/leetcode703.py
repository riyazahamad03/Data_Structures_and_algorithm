import heapq
class KthLargest:
    def __init__(self, k, nums: list[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int):
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


x = KthLargest(3, [4, 5, 8, 2])
print(x.add(3))
print(x.add(5))
print(x.add(10))
print(x.add(9))
print(x.add(4))
