class Solution:
    def numIslands(self, grid):
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        islandCount = 0

        # DFS algorithm
        def findIsland(i, j):
            visited[i][j] = 1
            if grid[i][j] == '1':
                if i < len(grid) - 1 and not visited[i + 1][j]:
                    findIsland(i+1, j)
                
                if j < len(grid[0]) - 1 and not visited[i][j + 1]:
                    findIsland(i, j+1)

                if j > 0 and not visited[i][j-1]:
                    findIsland(i, j-1)

                if i > 0 and not visited[i-1][j]:
                    findIsland(i-1,j)

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    findIsland(i,j)
                    islandCount += 1
                else:
                    visited[i][j] = 1

        return islandCount
    

solution = Solution()
print(solution.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

print(solution.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

print(solution.numIslands([
    ["1","0","1","1","1"],
    ["1","0","1","0","1"],
    ["1","1","1","0","1"]
]))

