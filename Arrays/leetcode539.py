from typing import List
import heapq


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []

        # Convert time points to total minutes since midnight
        for timepoint in timePoints:
            hr, mi = map(int, timepoint.split(":"))
            total_minutes = hr * 60 + mi
            minutes.append(total_minutes)

        # Sort the minutes list to calculate differences
        minutes.sort()

        # Initialize the minimum difference to be the largest possible (24 hours)
        min_diff = float("inf")

        # Compare consecutive time points
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])

        # Also check the difference between the first and last time point across midnight
        min_diff = min(min_diff, (1440 - minutes[-1] + minutes[0]))

        return min_diff


x = Solution()
print(x.findMinDifference(timePoints=["00:00", "23:59", "00:00"]))
