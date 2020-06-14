firstString = input()
secondString = input()

if len(firstString) == len(secondString):
     concatString = firstString + firstString
     print(secondString in concatString)
else:
    print(False)