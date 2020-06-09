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

    
                