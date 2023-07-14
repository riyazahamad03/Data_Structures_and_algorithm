class solution:
    def longestSubsequence(self, arr: list[int], difference: int):
        cnt = {}
        for i in range(len(arr)):
            diff = arr[i] - difference
            cnt[arr[i]] = 1 + cnt.get(diff, 0)
        return max(cnt.values())


x = solution()
print(x.longestSubsequence(arr=[1, 2, 3, 4], difference=1))
