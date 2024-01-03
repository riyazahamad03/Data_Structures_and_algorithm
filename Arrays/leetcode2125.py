class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        prev, res = None, 0
        for r in range(len(bank)):
            laser = 0
            for c in range(len(bank[r])):
                laser += int(bank[r][c])
            if prev:
                res += laser * prev
            if laser > 0:
                prev = laser
        return res


x = Solution()
print(x.numberOfBeams(["011001", "000000", "010100", "001000"]))
