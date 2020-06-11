#Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

usedChars = {}
inputString = ""


def hasUniqueChars():
    for char in inputString:
        if usedChars.get(char) == None:
           usedChars[char] = True
        else:
            return False
    return True

inputString = input()
print(hasRepeatedChars())



        

