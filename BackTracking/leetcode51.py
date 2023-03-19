class solution:
    def Nqueen(self , n:int):
        colCheck = set()
        posDiagCheck = set()
        negDiagCheck = set()

        res = []
        board = [["."]* n for _ in range(n)]

        def backTrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in colCheck or (r + c) in posDiagCheck or (r - c) in negDiagCheck:
                    continue

                colCheck.add(c)
                posDiagCheck.add(r + c)
                negDiagCheck.add(r - c)
                board[r][c] = "Q"

                backTrack(r + 1)

                colCheck.remove(c)
                posDiagCheck.remove(r + c)
                negDiagCheck.remove(r - c)
                board[r][c] = "."

        backTrack(0)
        return res
x = solution()
print(x.Nqueen(8))