class solution:
    def diagonalSum(self , mat : list[list[int]]):
        n = len(mat)
        s = 0
        for idex in range(n):
            s += mat[idex][idex]
            s += 0 if idex + idex == n - 1 else mat[idex][n - idex - 1]
        return s
x = solution()
print(x.diagonalSum([[1,2,3],
              [4,5,6],
              [7,8,9]]))