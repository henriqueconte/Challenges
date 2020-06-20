#Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

print("Enter the number of elements you want")

numberOfElements = int(input())
inputList = list()

print("Enter the elements")

for i in range(numberOfElements):
    inputList.append(int(input()))


print("Enter the kth number")

kth = int(input())

if kth < len(inputList):
    if kth < len(inputList) / 2:
        for i in range(kth):
            del inputList[i]
        print(inputList)
    else:
        newArray = list()
        for i in range(kth, len(inputList)):
            newArray.append(inputList[i])

        print(newArray)

else:
    print("kth out of range")