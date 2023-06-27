class Solution:
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                    if self.dfs(board, word, visited, i, j, 0):
                        return True
                    
        return False

    def dfs(self, board, word, visited, i, j, curr_size):
        if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or visited[i][j] or curr_size >= len(word) or word[curr_size] != board[i][j]:
            return False
        if curr_size == len(word) - 1:
            return True
        
        visited[i][j] = True
        exists = (self.dfs(board, word, visited, i+1, j, curr_size + 1) or
                              self.dfs(board, word, visited, i-1, j, curr_size + 1) or
                              self.dfs(board, word, visited, i, j+1, curr_size + 1) or
                                self.dfs(board, word, visited, i, j-1, curr_size + 1))
        visited[i][j] = False
        return exists

solution = Solution()
print(solution.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(solution.exist([["a","a"]], "aaa"))
print(solution.exist([["a"]], "a"))