class Solution:
    def convert(self, s, numRows):
        charMatrix = self.createMatrix(s, numRows)
        row = 0
        column = 0
        charCount = 0
        while charCount < len(s):
            while row < numRows and charCount < len(s):
                charMatrix[row][column] = s[charCount]
                row += 1
                charCount += 1
            row -= 1
            while row > 0 and charCount < len(s):
                row -= 1
                column += 1
                charMatrix[row][column] = s[charCount]
                charCount += 1
            row += 1
            if (numRows == 1):
                column += 1
                row = 0

        return self.output(charMatrix)
            
        
    def output(self, matrix):
        finalString = ""
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    finalString += matrix[i][j]

        return finalString

    def createMatrix(self, s, numRows):
        numColumns = len(s)
        return [([0] * numColumns) for i in range(numRows)]

a = Solution()

print(a.convert("PAYPALISHIRING", 4))
