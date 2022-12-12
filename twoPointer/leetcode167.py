class solution:
    def twoSum(self,numbers : list[int],target:int):
        i,j = 0,len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i] + numbers[j] > target:
                j-=1
            else:
                i+=1
x = solution()
print(x.twoSum([2,7,11,15],9)) 