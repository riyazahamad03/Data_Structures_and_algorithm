class solution:
    def spiralMatrix(self , n : int):
        res = [[0] * n for _ in range(n)]
        left , right , top , bottom = 0 , n , 0 , n
        idex = 1
        while left < right and top < bottom:
            for i in range(left , right):
                res[top][i] = idex
                idex += 1
            top += 1

            for i in range(top , bottom):
                res[i][right - 1] = idex
                idex += 1
            right -= 1 

            if not left < right and top < bottom:
                break

            for i in range(right - 1 , left - 1 , -1):
                res[bottom - 1][i] = idex
                idex += 1
            bottom -= 1

            for i in range(bottom - 1 , top - 1 , - 1):
                res[i][left] = idex
                idex += 1
            left += 1
        return res
x = solution()
print(x.spiralMatrix(3))