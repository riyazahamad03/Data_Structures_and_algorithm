class solution:
    def minCostClimbing(self,cost:list[int]):
        cost.append(0)
        for i in range(len(cost)-3,-1,-1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i+2] + cost[i])
        return min(cost[i],cost[i + 1])
x = solution()
print(x.minCostClimbing([10,15,20]))