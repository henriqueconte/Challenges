#Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin- drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

def isPalindrome(currentHash): 
    foundOneOdd = False

    for element in currentHash:
        if currentHash[element] % 2 != 0 and foundOneOdd:
            return False

        if currentHash[element] % 2 != 0:
            foundOneOdd = True
    
    return True

readChars = {}
inputString = input()
inputString = inputString.lower()

for char in inputString:
    if char != " ":
        if char in readChars:
            readChars[char] += 1
        else:
            readChars[char] = 1 

print(isPalindrome(readChars))

