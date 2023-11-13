import heapq


class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)

        def isVow(x):
            return x in "aeiouAEIOU"

        minHeap = []

        for i in range(len(s)):
            if isVow(s[i]):
                heapq.heappush(minHeap, (ord(s[i])))

        for i in range(len(s)):
            if isVow(s[i]):
                val = heapq.heappop(minHeap)
                s[i] = chr(val)
        return "".join(s)


x = Solution()
print(x.sortVowels(s="lEetcOde"))
