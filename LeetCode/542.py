import sys

class Solution:

    def updateMatrix(self, mat):
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] > 0:
                    top = mat[i - 1][j] if i > 0 else float('inf')
                    left = mat[i][j-1] if j > 0 else float('inf')
                    mat[i][j] = 1 + min(left,top)

        for i in range(len(mat) - 1, -1, -1):
            for j in range(len(mat[0]) - 1, -1, -1):
                if mat[i][j] > 0:
                    bottom = mat[i + 1][j] if i < len(mat) - 1 else float('inf')
                    right = mat[i][j+1] if j < len(mat[0]) - 1 else float('inf') 
                    mat[i][j] = min(1 + bottom, 1 + right, mat[i][j])

        return mat

solution = Solution()
print(solution.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
print(solution.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))