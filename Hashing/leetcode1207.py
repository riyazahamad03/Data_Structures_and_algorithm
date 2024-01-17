class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count = {}
        for i in arr:
            count[i] = 1 + count.get(i, 0)

        Set = set()
        for i, e in count.items():
            if e in Set:
                return False
            Set.add(e)
        return True


x = Solution()
print(x.uniqueOccurrences([1, 2, 2, 1, 1, 3]))
