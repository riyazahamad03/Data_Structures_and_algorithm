class solution:
    def carFleet(self , position : list[int] , speed : list[int] , target : int):
        cars = [[p,s] for p,s in zip(position , speed)]
        cars = sorted(cars)
        stack = []
        for idex in range(len(cars)-1, -1 ,-1):
            p,s = cars[idex]
            stack.append((target - p)/s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
x = solution()
print(x.carFleet([10,8,0,5,3] , [2,4,1,1,3] , 12))