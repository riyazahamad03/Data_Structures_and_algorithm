class SnapshotArray:
    def __init__(self, length: int):
        self.snaps = [[(0, 0)] for _ in range(length)]
        self.snapsCalled = 0

    def set(self, index: int, val: int) -> None:
        self.snaps[index].append((self.snapsCalled, val))

    def snap(self) -> int:
        self.snapsCalled += 1
        return self.snapsCalled - 1

    def get(self, index: int, snap_id: int) -> int:
        history = self.snaps[index]
        l, r = 0, len(history) - 1
        while l <= r:
            m = (l + r)//2
            if history[m][0] == snap_id:
                l = m + 1
            else:
                r = m - 1
        return history[r][1]


x = SnapshotArray(3)
print(x.set(0, 5))
print(x.snap())
print(x.set(0, 6))
print(x.get(0, 0))
