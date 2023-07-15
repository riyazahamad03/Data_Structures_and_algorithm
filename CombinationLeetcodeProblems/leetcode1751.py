class solution:
    def maxValue(self, events: list[list[int]], k: int):
        events.sort()
        n = len(events)
        cache = {}
        starts = [elem[0] for elem in events]

        def dfs(currIdx, cnt):
            if currIdx == n or cnt == 0:
                return 0
            if (currIdx, cnt) in cache:
                return cache[(currIdx, cnt)]

            nxtIndex = self.binSearch(starts, events[currIdx][1])
            cache[(currIdx, cnt)] = max(dfs(currIdx + 1, cnt),
                                        events[currIdx][2] + dfs(nxtIndex, cnt - 1))
            return cache[(currIdx, cnt)]
        return dfs(0, k)

    def binSearch(self, arr, tar):
        l, r = 0, len(arr)
        while l < r:
            m = (l + r)//2
            if arr[m] <= tar:
                l = m + 1
            else:
                r = m
        return l


x = solution()
print(x.maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 1]], k=2))
