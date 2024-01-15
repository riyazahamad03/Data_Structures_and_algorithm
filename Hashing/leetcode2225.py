from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count = {}
        res = [set(), set()]
        for w, l in matches:
            count[l] = count.get(l, 0) + 1
        for w, l in matches:
            if w not in count:
                res[0].add(w)
        for l, c in count.items():
            if c == 1:
                res[1].add(l)
        res[0] = sorted(res[0])
        res[1] = sorted(res[1])
        return res


x = Solution()
print(
    x.findWinners(
        matches=[
            [1, 3],
            [2, 3],
            [3, 6],
            [5, 6],
            [5, 7],
            [4, 5],
            [4, 8],
            [4, 9],
            [10, 4],
            [10, 9],
        ]
    )
)
