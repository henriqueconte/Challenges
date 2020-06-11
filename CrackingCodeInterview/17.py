#Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
#bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

# A basic code for matrix input from user 
  
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrix = [[0 for x in range(C)] for y in range(R)] 
rotatedMatrix = [[0 for x in range(R)] for y in range(C)]

print("Enter the entries rowwise:") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    for j in range(C):      # A for loop for column entries 
         newValue = int(input())
         matrix[i][j] = newValue
         rotatedMatrix[j][R - i - 1] = newValue
  
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 

print()

for i in range(C): 
    for j in range(R): 
        print(rotatedMatrix[i][j], end = " ") 
    print() 