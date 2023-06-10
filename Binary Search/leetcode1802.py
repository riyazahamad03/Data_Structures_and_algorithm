class solution:
    def maxValue(self, n: int, index: int, maxSum: int):
        left, right = index, n - index - 1
        low, high = 1, maxSum
        res = 0
        while low <= high:
            mid = (low + high)//2
            arrSum, m = mid, mid - 1

            # right subArray Sum Finding
            if right <= m:
                arrSum += m*(m + 1)//2 - (m - right) * (m - right + 1)//2
            else:
                arrSum += m * (m + 1)//2 + 1 * (right - m)

            # leftSubArray Sum Finding
            if left <= m:
                arrSum += m * (m + 1)//2 - (m - left)*(m - left + 1)//2
            else:
                arrSum += m*(m+1)//2 + (1) * (left - m)

            if (arrSum <= maxSum):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res


x = solution()
print(x.maxValue(n=4, index=2,  maxSum=6))
