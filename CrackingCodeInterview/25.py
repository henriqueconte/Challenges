#Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the Vs digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

print("Enter the number of elements you want for the first list")

numberOfElements = int(input())
firstInputList = list()

print("Enter the elements")

for i in range(numberOfElements):
    firstInputList.append(int(input()))


print("Enter the number of elements you want for the second list")

numberOfElements = int(input())
secondInputList = list()

print("Enter the elements")

for i in range(numberOfElements):
    secondInputList.append(int(input()))



firstNumber = ""
secondNumber = ""

for i in range(len(firstInputList)):
    firstNumber += str(firstInputList[len(firstInputList) - i - 1])

for i in range(len(secondInputList)):
    secondNumber += str(secondInputList[len(secondInputList) - i - 1])

finalSum = int(firstNumber) + int(secondNumber)
finalArray = list()

for element in str(finalSum):
    finalArray.insert(0, element)

print(finalArray, "That is: ", finalSum)
