def isValid(infoList):
    passportInfo = {}
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

    for element in infoList:
        passportInfo[element[0]] = element[1]

    ###########################################
    #                 PART 1                  #
    ###########################################

    for element in requiredFields:
        if element not in passportInfo:
            if element != "cid":
                return False

    return True
    
def parseInput():
    validPassportsCount = 0
    infoList = []
    
    parsedInputFile = fileContent.strip().split('\n\n')

    for line in parsedInputFile:
        lineElements = line.split("\n")
        for groupAttribute in lineElements:
            attributeList = groupAttribute.split()
            for element in attributeList:
                keyValueElement = element.split(":")
                infoList.append(keyValueElement)
        
        if isValid(infoList):
            validPassportsCount += 1

        infoList = []

    return validPassportsCount

with open("inputs/Day4Input.txt") as f:
    fileContent = f.read()
passportList = []

print("Number of valid passports: ", parseInput())
