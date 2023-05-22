class solution:
    def topKfrequent(self,nums:list[int],k:int):
        # counting hashTable
        dCount = {}

        for i in range(len(nums)):
            dCount[nums[i]] = 1 + dCount.get(nums[i] , 0)
        
        # frequency array  
        frequency = [[] for _ in range(len(nums) + 1)]
        
        #storing the count based element in frequency array 
        for element,count in dCount.items():
            frequency[count].append(element)

        # iterating from reverse order and storing in resultant array
        res = []
        
        for idex in range(len(frequency)-1,-1,-1):
            for element in frequency[idex]:
                res.append(element)
                if k == len(res):
                    return res
x = solution()
print(x.topKfrequent([1,1,1,2,2,3], 2))
            
# time complexity O(N)
# space complexity O(2N)