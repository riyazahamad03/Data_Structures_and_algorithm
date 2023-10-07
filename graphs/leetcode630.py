import heapq


class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        # dp = {}

        # def dfs(idx, cTaken):
        #     if idx == len(courses):
        #         return 0

        #     # key = (idx, cTaken)
        #     # if key in dp:
        #     #     return dp[key]

        #     crs, deadLine = courses[idx]

        #     if cTaken + crs <= deadLine:
        #         res = max(dfs(idx + 1, cTaken + crs) + 1, dfs(idx + 1, cTaken))
        #     else:
        #         res = dfs(idx + 1, cTaken)

        #     # dp[key] = res
        #     return res

        # return dfs(0, 0)

        maxHeap = []
        time = 0
        for crs, lastDay in courses:
            if crs <= lastDay:
                if crs + time <= lastDay:
                    val = -1 * (crs)
                    heapq.heappush(maxHeap, val)
                    time += crs
                else:
                    val = -1 * maxHeap[0]
                    if val > crs:
                        poppedVal = -1 * heapq.heappop(maxHeap)
                        time -= val
                        time += crs
                        heapq.heappush(maxHeap, -1 * crs)
        return len(maxHeap)


x = Solution()
print(x.scheduleCourse(courses=[[100, 200], [
      200, 1300], [1000, 1250], [2000, 3200]]))
