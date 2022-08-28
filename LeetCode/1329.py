class Solution:
    def sortList(self, elements):
        return elements.sort()

    def diagonalSort(self, mat):
        for a in range(len(mat)):
            for i in range(len(mat) - 1):
                for j in range(len(mat[i]) - 1):
                    if i < len(mat) and j < len(mat[i]):
                        if mat[i][j] > mat[i+1][j+1]:
                            mat[i][j], mat[i+1][j+1] = mat[i+1][j+1], mat[i][j]
                            

        return mat

a = Solution()

def make_zeros(n_rows: int, n_columns: int):
    matrix = []
    for i in range(n_rows):
        matrix.append([0] * n_columns)
    return matrix

listToSort = [1, 6, 3, 2, 1]
matrixToSort = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]

print(matrixToSort)
matrixToSort = a.diagonalSort(matrixToSort)
print(matrixToSort)


