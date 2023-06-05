class Solution:
    def coinChange(self, coins, amount):
        partialSums = [-1 for i in range(amount + 1)]

        def minimumAmountOfCoins(coins, amount):
            if amount == 0:
                return 0

            if partialSums[amount] != -1:
                return partialSums[amount]

            minimumCoins = 10e5
        
            for coin in coins:
                if amount - coin >= 0:
                    minimumCoins = min(minimumCoins, minimumAmountOfCoins(coins, amount - coin) + 1)

            partialSums[amount] = minimumCoins
            
            return minimumCoins
        
        coinsCount = minimumAmountOfCoins(coins, amount)

        if coinsCount == 10e5:
            return -1
        else:
            return coinsCount
        

        
solution = Solution()
print(solution.coinChange([1,2,5], 11))
print(solution.coinChange([2], 3))
print(solution.coinChange([1], 0))
print(solution.coinChange([186,419,83,408], 6249))

# 6249 - 5866
# 383 

# amount % min(coins) = total amount of combinations we can have
# Tree 

# coins x coins
# 0 + 1
# 0 + 2
# 0 + 1 + 2

# 3, 10, 11 -> 122
# 0, 0, 11 -> 121 /132 (-9)
# 0, 1, 9 -> 
# 3, -> 10