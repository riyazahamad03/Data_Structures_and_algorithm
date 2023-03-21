class solution:
    def nQueens(self , n:int):
        res = 0
        posDiagCheck = set()
        negDiagCheck = set()
        colCheck = set()


        def backTrack(r):
            if r == n:
                nonlocal res
                res += 1
                return
            for c in range(n):
                if c in colCheck or (r + c) in posDiagCheck or (r - c) in negDiagCheck:
                    continue
                colCheck.add(c)
                posDiagCheck.add(r + c)
                negDiagCheck.add(r - c)

                backTrack(r + 1)

                colCheck.remove(c)
                posDiagCheck.remove(r + c)
                negDiagCheck.remove(r - c)
        backTrack(0)
        return res
x = solution()
print(x.nQueens(5))