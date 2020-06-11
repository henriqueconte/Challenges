#One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

def replaceChar(firstString, secondString):
    hasReplaced = False

    for i in range(len(firstString)):
        if hasReplaced and firstString[i] != secondString[i]:
            return False
        elif firstString[i] != secondString[i]:
            hasReplaced = True
    
    return True

def insertChar(firstString, secondString):
    hasInserted = False

    for i in range(len(firstString)):
        if hasInserted == False:
            if firstString[i] != secondString[i]:
                hasInserted = True
        elif firstString[i] != secondString[i + 1]:
            return False
        
    return True

def deleteChar(firstString, secondString):
    hasDeleted = False

    for i in range(len(secondString)):
        if hasDeleted == False:
            if firstString[i] != secondString[i]:
                hasDeleted = True
        elif firstString[i] != secondString[i - 1]:
            return False
        
    return True    

firstString = input()
secondString = input()

if len(firstString) == len(secondString):
    print(replaceChar(firstString, secondString))

elif len(firstString) + 1 == len(secondString):
    print(insertChar(firstString, secondString))

elif len(firstString) - 1 == len(secondString):
    print(deleteChar(firstString, secondString))

else:
    print(False)