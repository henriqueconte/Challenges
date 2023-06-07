class Solution:
    def orangesRotting(self, grid):
        rotten_minutes_grid = [[100 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        longest_rotten_day = 0
        rotten_oranges_count = 0
        total_oranges_count = 0

        def dfs(i, j, rotten_minutes):
            rotten_minutes_grid[i][j] = min(rotten_minutes_grid[i][j], rotten_minutes)
            
            if i < len(grid) - 1 and grid[i+1][j] == 1 and rotten_minutes_grid[i][j] < rotten_minutes_grid[i+1][j]:
                dfs(i+1,j,rotten_minutes + 1)

            if j < len(grid[0]) - 1 and grid[i][j+1] == 1 and rotten_minutes_grid[i][j] < rotten_minutes_grid[i][j+1]:
                dfs(i,j+1,rotten_minutes + 1)

            if i > 0 and grid[i-1][j] == 1 and rotten_minutes_grid[i][j] < rotten_minutes_grid[i-1][j]:
                dfs(i-1,j,rotten_minutes + 1)

            if j > 0 and grid[i][j-1] == 1 and rotten_minutes_grid[i][j] < rotten_minutes_grid[i][j-1]:
                dfs(i,j-1,rotten_minutes + 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total_oranges_count += 1
                elif grid[i][j] == 2:
                    total_oranges_count += 1
                    dfs(i, j, 0)
                    
        for i in range(len(rotten_minutes_grid)):
            for j in range(len(rotten_minutes_grid[0])):
                if rotten_minutes_grid[i][j] != 100:
                    rotten_oranges_count += 1
                    longest_rotten_day = max(longest_rotten_day, rotten_minutes_grid[i][j])
                
        if total_oranges_count == rotten_oranges_count:
            return longest_rotten_day
        else:
            return -1
    
solution = Solution()
print(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(solution.orangesRotting([[0,2]]))
print(solution.orangesRotting([
    [2,1,1],
    [1,1,1],
    [0,1,2]]))

[[0, 1, 2], 
 [1, 2, 1], 
 [100, 1, 0]]
# Iterate over all the grid
# If it finds a unvisited rotten orange, 
    # Run DFS to search the farthest fresh orange
    # Intersections can happen!



# Alternative:
    # Traverse grid and save all the rotten oranges. Count the fresh oranges. 
    # Then, do a BFS for each rotten orange until there are no oranges to rot
    # If the final amount of rotten oranges is different from the fresh oranges, return -1

# Alternative (let's implement this one):
    # Do a DFS every time we find a rotten orange
    # Save rotten days for each orange. Only go to next orange if rotten days > current rotten days.
    # Save the highest amount of rotten days 