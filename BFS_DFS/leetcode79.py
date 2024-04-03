class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(i, r, c):
            if i == len(word):
                return True
            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or word[i] != board[r][c]
                or (r, c) in visit
            ):
                return False
            visit.add((r, c))
            res = False
            res = res or dfs(i + 1, r + 1, c)
            res = res or dfs(i + 1, r - 1, c)
            res = res or dfs(i + 1, r, c + 1)
            res = res or dfs(i + 1, r, c - 1)
            visit.remove((r, c))
            return res

        visit = set()
        for r in range(rows):
            for c in range(cols):
                if word[0] == board[r][c]:
                    # visit = set()
                    if dfs(0, r, c):
                        return True
        return False


x = Solution()
print(
    x.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED",
    )
)
