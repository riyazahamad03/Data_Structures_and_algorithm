class solution:
    def checkStraightLine(self , coordinates : list[list[int]]):
        xDiff = coordinates[1][0] - coordinates[0][0]
        yDiff = coordinates[1][1] - coordinates[0][1]

        for i in range(2 , len(coordinates)):
            currX = coordinates[i][0] - coordinates[i - 1][0]
            currY = coordinates[i][1] - coordinates[i - 1][1]

            if currY * xDiff != currX * yDiff:
                return False
        return True 
x = solution()
print(x.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))