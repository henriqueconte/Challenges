class Solution:
    def uniquePaths(self, m, n):
        dp = [[-1 for i in range (n)] for j in range(m)]
        return self.dfs(0, 0, m-1, n-1, dp)
    
    def dfs(self, i, j, m, n, dp):
        if i > m or j > n:
            return 0
        
        if i == m or j == n:
            return 1
        
        if dp[i][j] != -1:
            return dp[i][j]

        dp[i][j] = self.dfs(i+1, j, m, n, dp) + self.dfs(i, j+1, m, n, dp)

        return dp[i][j]

solution = Solution()
print(solution.uniquePaths(3, 7))
print(solution.uniquePaths(3, 2))
# 22 - > 24 -> 

# 8

# 32 - 2 - 1 - 5