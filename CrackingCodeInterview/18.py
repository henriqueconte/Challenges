def zeroMatrix(currentMatrix, R, C):
    zeroRows = {}
    zeroColumns = {}
    newMatrix = currentMatrix

    for i in range(R):

        if i not in zeroRows:
           
            for j in range(C):
                
                if j not in zeroColumns:

                    if matrix[i][j] == 0:
                        for column in range(C):
                            newMatrix[i][column] = 0
                        for row in range(R):
                            newMatrix[row][j] = 0
                        
                        zeroRows[i] = True
                        zeroColumns[j] = True
                        break

    return newMatrix
                        

#Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrix = [[0 for x in range(C)] for y in range(R)] 

print("Enter the entries rowwise:") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    for j in range(C):      # A for loop for column entries 
         newValue = int(input())
         matrix[i][j] = newValue
# For printing the matrix 

newMatrix = zeroMatrix(matrix, R, C)

for i in range(R): 
    for j in range(C): 
        print(newMatrix[i][j], end = " ") 
    print() 

print()