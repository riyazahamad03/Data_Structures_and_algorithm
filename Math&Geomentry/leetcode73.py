class solution:
    def setMatrixZero(self,matrix:list[int]):
        row,col = len(matrix),len(matrix[0])
        rowZero = False

        # checking rows and cols to make zero
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        # setting matrix to zero
        for r in range(1,row):
            for c in range(1,col):
                if matrix[r][0] == 0  or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # checking for top col
        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0] = 0
        # checking for top row
        if rowZero:
            for c in range(col):
                matrix[0][c] = 0
        return matrix
x = solution()
print(x.setMatrixZero([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
