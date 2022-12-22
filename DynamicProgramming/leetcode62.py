class solution:
    def uniquePaths(self,m:int,n:int):
        row = [1] * n
        for _ in range(m-1):
            nRow = [1] * n
            for j in range(n-2,-1,-1):
                nRow[j] = nRow[j+1] + row[j]
            row = nRow
        return row[0]
x = solution()
print(x.uniquePaths(3,7))

