treesMaps = []

inputFile = open("inputs/Day3Input.txt")
for line in inputFile:
    treeLine = line.split()[0]
    treesMaps.append(treeLine)

def traversing(rightSlope, downSlope):
    numberOfTrees = 0
    i = 0
    rowPosition = 0
    
    while i < len(treesMaps):
        rowPositionQuotient = rowPosition % len(treesMaps[i])
        if treesMaps[i][rowPositionQuotient] == "#":
            numberOfTrees += 1
        i += downSlope
        rowPosition += rightSlope
        
        if i == len(treesMaps) and downSlope > 1:
            if treesMaps[i-1][rowPositionQuotient] == "#":
                numberOfTrees += 1

    return numberOfTrees
             

###########################################
#                 PART 1                  #
###########################################
print("Number of trees encoutered for Right slope 3 and Down slope 1 ", traversing(3, 1))


###########################################
#                 PART 2                  #
###########################################
treesCountList = [
    traversing(1,1),
    traversing(3,1),
    traversing(5,1),
    traversing(7,1),
    traversing(1,2)
]
treesMultiplication = 1

for element in treesCountList:
    treesMultiplication = treesMultiplication * element

print("Number of trees encoutered for Right slope 1 and Down slope 1 ", traversing(1, 1))
print("Number of trees encoutered for Right slope 3 and Down slope 1 ", traversing(3, 1))
print("Number of trees encoutered for Right slope 5 and Down slope 1 ", traversing(5, 1))
print("Number of trees encoutered for Right slope 7 and Down slope 1 ", traversing(7, 1))
print("Number of trees encoutered for Right slope 1 and Down slope 2 ", traversing(1, 2))
print("Multiplication of all trees: ", treesMultiplication)
