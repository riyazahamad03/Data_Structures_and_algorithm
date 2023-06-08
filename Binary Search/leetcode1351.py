class solution:
    def countNegative(self , grid : list[list[int]]):
        n , res = len(grid[0]) , 0
        for row in grid:
            l , r = 0 , n - 1
            while l <= r:
                m = (l + r)//2
                if row[m] < 0:
                    r = m - 1
                else:
                    l = m + 1
            res += n - l
        return res
x = solution()
print(x.countNegative([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))