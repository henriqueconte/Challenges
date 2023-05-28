class Solution:
    memo = []
    for i in range(50):
        memo.append(-1)
    def climbStairs(self, n):
        if n == 1: 
            return 1
        if n == 2:
            return 2
        
        if self.memo[n] != -1:
            return self.memo[n]
        
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]
        

solution = Solution()

print(solution.climbStairs(6))

# 1
# 2
# 3
# 5
# 8

# 38
# 19 -> 1
# 20 -> 

3, 2

4, 2

5, 3

6, 3

7, 4

8, 4

# 19

