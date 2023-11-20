import heapq


class Solution:
    def leftmostBuildingQueries(
        self, heights: list[int], queries: list[list[int]]
    ) -> list[int]:
        ans = [-1 for i in range(len(queries))]
        needed = {i: [] for i in range(len(heights))}

        for i in range(len(queries)):
            q1, q2 = queries[i]

            left = min(q1, q2)
            right = max(q1, q2)

            if left == right:
                ans[i] = left
                continue

            if heights[left] < heights[right]:
                ans[i] = right
            else:
                needed[right].append([max(heights[left], heights[right]), i])

        minHeap = []

        for i in range(len(heights)):
            while minHeap:
                if heights[i] > minHeap[0][0]:
                    height, idx = heapq.heappop(minHeap)
                    ans[idx] = i
                else:
                    break

            if len(needed[i]) > 0:
                for val in needed[i]:
                    heapq.heappush(minHeap, val)

        return ans


x = Solution()
print(
    x.leftmostBuildingQueries(
        heights=[6, 4, 8, 5, 2, 7], queries=[[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]
    )
)
