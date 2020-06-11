# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

firstString = input()
secondString = input()

firstString = sorted(firstString)
secondString = sorted(secondString)

if firstString == secondString:
    print(True)
else:
    print(False)

