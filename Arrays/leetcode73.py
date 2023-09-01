class solution:
    def setZeros(self, matrix: list[list[int]]):
        row, col = len(matrix), len(matrix[0])
        rowZero = False
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowZero = True
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if not matrix[0][0]:
            for i in range(col):
                matrix[0][i] = 0
        if rowZero:
            for i in range(row):
                matrix[i][0] = 0

        return matrix


x = solution()
print(x.setZeros(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
