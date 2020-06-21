#Palindrome: Implement a function to check if a linked list is a palindrome


def checkPalindrome(currentList):
    for i in range(len(currentList)):
        if i > len(currentList) / 2:
            return True
        if currentList[i] != currentList[len(currentList) - i - 1]:
            return False   

print("Enter the number of elements you want")

numberOfElements = int(input())
inputList = list()

print("Enter the elements")

for i in range(numberOfElements):
    inputList.append(int(input()))

print(checkPalindrome(inputList))

