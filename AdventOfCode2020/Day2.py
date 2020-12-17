class PasswordValidator:
    def __init__(self, minCharCount, maxCharCount, ruleChar, password):
        self.minCharCount = int(minCharCount)
        self.maxCharCount = int(maxCharCount)
        self.ruleChar = ruleChar
        self.password = password


    ###########################################
    #                 PART 1                  #
    ###########################################
    def checkFirstPasswordPolicy(self):
        charCount = 0

        for letter in self.password:
            if letter == self.ruleChar:
                charCount += 1

        if charCount >= self.minCharCount and charCount <= self.maxCharCount:
            return True
        else:
            return False 
        
    ###########################################
    #                 PART 2                  #
    ###########################################
    def checkSecondPasswordPolicy(self):
        foundChar = False

        if self.minCharCount > len(self.password):
            return False
            
        elif self.password[self.minCharCount - 1] == self.ruleChar:
            if self.maxCharCount <= len(self.password):
                if self.password[self.maxCharCount - 1] == self.ruleChar:
                    return False
            return True

        elif self.maxCharCount <= len(self.password):
            if self.password[self.maxCharCount - 1] == self.ruleChar:
                return True

def parseInput(inputLine):
    inputLine = inputLine.split(" ")
    charBoundaries = inputLine[0].split("-")
    ruleChar = inputLine[1].split(":")[0]
    password = inputLine[2]
    return PasswordValidator(charBoundaries[0], charBoundaries[1], ruleChar, password)

firstPolicyValidPasswordsCount = 0
secondPolicyValidPasswordsCount = 0
inputFile = open("inputs/Day2Input.txt")
for line in inputFile:
    newPasswordValidator = parseInput(line)
    if newPasswordValidator.checkFirstPasswordPolicy():
        firstPolicyValidPasswordsCount += 1

    if newPasswordValidator.checkSecondPasswordPolicy():
        secondPolicyValidPasswordsCount += 1


print("Number of valid passwords on first policy: ", firstPolicyValidPasswordsCount)
print("Number of valid passwords on second policy: ", secondPolicyValidPasswordsCount)
    

