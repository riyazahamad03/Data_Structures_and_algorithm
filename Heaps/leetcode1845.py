import heapq


class SeatManager:
    def __init__(self, n: int):
        self.minHeap = [i for i in range(1, n + 1)]

    def reserve(self) -> int:
        return heapq.heappop(self.minHeap)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.minHeap, seatNumber)


x = SeatManager(5)
print(x.reserve())
print(x.reserve())
x.unreserve(2)
x.unreserve(1)
