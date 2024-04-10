from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort()
        res = [0] * (len(deck))
        q = deque(range(len(deck)))
        for e in deck:
            idx = q.popleft()
            res[idx] = e

            if q:
                q.append(q.popleft())

        return res


x = Solution()
print(x.deckRevealedIncreasing(deck=[17, 13, 11, 2, 3, 5, 7]))
