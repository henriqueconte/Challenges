class Solution:
    def maxProfit(self, prices):
        profit = 0
        buyIndex = 0
        sellIndex = 1

        while (sellIndex < len(prices)):
            if prices[sellIndex] - prices[buyIndex] > profit:
                profit = prices[sellIndex] - prices[buyIndex]
            
            if prices[sellIndex] < prices[buyIndex]:
                buyIndex = sellIndex

            sellIndex += 1

        return profit

solution = Solution()

print(solution.maxProfit([7,1,5,3,6,4,0,10,2,11]))