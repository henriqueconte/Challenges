#Remove Dups: Write code to remove duplicates from an unsorted linked list.

print("Enter the number of elements you want")

numberOfElements = int(input())
inputList = list()

for i in range(numberOfElements):
    inputList.append(input())


readElements = {}

print(inputList)

for element in inputList:
    if element in readElements:
        inputList.remove(element)
    else:
        readElements[element] = True

print(inputList)
    

