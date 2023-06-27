import heapq


class solution:
    def kSmallestPair(self, list1: list[int], list2: list[int], k: int):
        q = [(list1[0] + list2[0], (0, 0))]
        res, visited = [], set((0, 0))
        while k and q:
            val, (i, j) = heapq.heappop(q)
            res.append([list1[i], list2[j]])

            if (i + 1) < len(list1) and (i + 1, j) not in visited:
                heapq.heappush(q, (list1[i + 1] + list2[j], (i + 1, j)))
                visited.add((i + 1, j))
            if (j + 1) < len(list2) and (i, j + 1) not in visited:
                heapq.heappush(q, (list1[i] + list2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))
            k -= 1
        return res


x = solution()
print(x.kSmallestPair([1, 7, 11], [2, 4, 6], 3))
