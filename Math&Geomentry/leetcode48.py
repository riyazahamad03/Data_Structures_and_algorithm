# 48. Rotate Image
class solution:
    def rotate90deg(self,matrix:list[list[int]]):
        l,r = 0, len(matrix[0])-1
        while l <= r:
            for i in range(r-l):
                t,b = l,r
                topLeft = matrix[t][l + i]
                matrix[t][l + i] = matrix[b - i][l] 
                matrix[b - i][l] = matrix[b][r - i] 
                matrix[b][r - i] = matrix[t + i][r]  
                matrix[t + i][r] = topLeft
            l += 1
            r -= 1
        return matrix
x = solution()
print(x.rotate90deg([[1,2,3],[4,5,6],[7,8,9]]))
