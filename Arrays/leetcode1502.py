class solution:
    def canMakeArithmeticProgression(self , arr : list[int]):
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2 , len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True
x = solution()
print(x.canMakeArithmeticProgression([3,5,1]))