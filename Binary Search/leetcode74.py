class solution:
    def search2D(self,matrix:list[list[int]],target:int):
        rows,cols = len(matrix),len(matrix[0])
        # binary search for finding the target row
        top,bottom = 0,rows-1
        while top <= bottom:
            row = (top + bottom)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        if not (top<=bottom):
            return False
        
        # doing binary search in the column
        l,r = 0,cols-1
        row = (top + bottom)//2
        while l<=r:
            mid = (l + r )//2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return True
x = solution()
print(x.search2D([[1,3,5,7],[10,11,16,20],[23,30,34,60]],121))
# timeComplexity - O(logm * logn)