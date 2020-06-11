#String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3, If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).


def compressString(currentString):
    if len(currentString) > 0:
        readingChar = currentString[0]
        charCount = 0
        resultString = ""

        for element in currentString:
            if element == readingChar:
                charCount += 1
            else:
                resultString = resultString + readingChar + str(charCount)
                readingChar = element
                charCount = 1
        resultString = resultString + readingChar + str(charCount)

        if len(resultString) >= len(currentString):
            return currentString
        else:
            return resultString
    else:
        return "Empty string"


inputString = input()

print(compressString(inputString))

    
                