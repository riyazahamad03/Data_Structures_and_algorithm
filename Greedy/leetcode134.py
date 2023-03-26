class solution:
    def canCompleteCircuit(self , gas : list[int] , cost : list[int]):
        if sum(gas) < sum(cost):
            return -1
        tot , res = 0 , 0
        for i in range(len(gas)):
            tot += gas[i] - cost[i]
            if tot < 0:
                tot = 0
                res = i + 1
        return res
x = solution()
print(x.canCompleteCircuit([1,2,3,4,5] , [3,4,5,1,2]))