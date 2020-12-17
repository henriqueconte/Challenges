inputList = {}

inputFile = open("inputs/Day1Input.txt")
for line in inputFile:
    line = line.split()
    inputList[line[0]] = True


def findPair(goalSum, currentValue):
    if str(goalSum - intElement) in inputList:
        return goalSum - intElement
    else:
        return None



###########################################
#                 PART 1                  #
###########################################

# for element in inputList:
#     intElement = int(element)

#     if str(2020 - intElement) in inputList:
#         print("Element A: ", intElement)
#         print("Element B: ", 2020 - intElement)
#         print("Mult of Element A and B: ", intElement * (2020 - intElement))  
#         break   

for element in inputList:
    intElement = int(element)
    if findPair(2020, intElement):
        print("Element A: ", intElement)
        print("Element B: ", 2020 - intElement)
        print("Mult of Element A and B: ", intElement * (2020 - intElement))  
        break   

###########################################
#                 PART 2                  #
###########################################     

for element in inputList:
    intElement = int(element)
    for childElement in inputList:
        intChildElement = int(childElement)
        if str(2020 - intElement - intChildElement) in inputList:
            print("Element A: ", intElement)
            print("Element B: ", intChildElement)
            print("Element C: ", 2020 - intElement - intChildElement)
            print("Mult of Element A, B and C: ", intElement * intChildElement * (2020 - intElement - intChildElement)) 
            break


 