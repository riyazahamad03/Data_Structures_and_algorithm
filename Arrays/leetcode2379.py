class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = k

        l = 0
        min_col = 0
        for r in range(len(blocks)):
            if blocks[r] == "W":
                min_col += 1

            if r - l + 1 == k:
                res = min(res, min_col)

                if blocks[l] == "W":
                    min_col -= 1
                l += 1
        return res


x = Solution()
print(x.minimumRecolors("WBBWWBBWBW", 7))
