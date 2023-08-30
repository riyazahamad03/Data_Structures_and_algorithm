import heapq


class MedianFinder:

    def __init__(self):
        # maxHeap    minHeap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # maxHeap's small number should be less than minHeaps's number
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            v1 = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, v1)
        # uneven Size
        if len(self.small) > len(self.large) + 1:
            v1 = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, v1)
        if len(self.large) > len(self.small) + 1:
            v1 = heapq.heappop(self.large)
            heapq.heappush(self.small, (-1 * v1))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0])/2


obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(4)
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
