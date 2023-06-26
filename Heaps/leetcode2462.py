import heapq


class solution:
    def totalCost(self, costs: list[int], k: int, candidates: int):
        headWorkers = costs[:candidates]
        tailWorkers = costs[max(candidates, len(costs) - candidates):]

        nxtHead, nxtTail = candidates, max(
            len(costs) - candidates - 1, candidates - 1)

        heapq.heapify(headWorkers)
        heapq.heapify(tailWorkers)

        res = 0
        for _ in range(k):
            if not tailWorkers or (headWorkers and headWorkers[0] <= tailWorkers[0]):
                res += heapq.heappop(headWorkers)

                if nxtHead <= nxtTail:
                    heapq.heappush(headWorkers, costs[nxtHead])
                    nxtHead += 1
            else:
                res += heapq.heappop(tailWorkers)

                if nxtHead <= nxtTail:
                    heapq.heappush(tailWorkers, costs[nxtTail])
                    nxtTail -= 1
        return res


x = solution()
print(x.totalCost(costs=[17, 12, 10, 2, 7, 2, 11, 20, 8], k=3, candidates=4))
