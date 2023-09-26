import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = collections.Counter(s)
        stack = []
        visit = set()
        for c in s:
            count[c] -= 1
            if c in visit:
                continue
            while stack and ord(stack[-1]) > ord(c) and count[stack[-1]] > 0:
                visit.remove(stack.pop())
            visit.add(c)
            stack.append(c)
        return "".join(stack)


x = Solution()
print(x.removeDuplicateLetters("bcabc"))
