class solution:
    def kidsWithCandies(self , candies : list[int] , extraCandies : int):
        maxCandies = max(candies)
        for i in range(len(candies)):
            candies[i] = True if candies[i] + extraCandies >= maxCandies else False
        return candies
x = solution()
print(x.kidsWithCandies([2,3,5,1,3] , 3))