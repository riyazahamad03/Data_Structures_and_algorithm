'''
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]

Output: 5

'''

class solution:
    def maxProfit(self,prices : list[int]):
        maxProfit = 0
        left,right = 0,1
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit,profit) 
            else:
                left = right

            right += 1
        return maxProfit
x = solution()
print(x.maxProfit([7,1,5,3,6,4]))