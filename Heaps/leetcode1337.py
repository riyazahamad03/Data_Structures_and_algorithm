import heapq


class solution:
    def kWeakestRow(self, mat: list[list[int]], k: int):
        res = []
        minHeap = []

        for row in range(len(mat)):
            heapq.heappush(minHeap, (mat[row].count(1), row))
        while k:
            cnt, row = heapq.heappop(minHeap)
            res.append(row)
            k -= 1
        return res


x = solution()
print(x.kWeakestRow(mat=[[1, 1, 0, 0, 0],
                         [1, 1, 1, 1, 0],
                         [1, 0, 0, 0, 0],
                         [1, 1, 0, 0, 0],
                         [1, 1, 1, 1, 1]],
                    k=3))
