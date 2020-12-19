inputFile = open("inputs/Day6Input.txt")
answeredQuestions = {}
totalAnswersSum = 0
everyoneAnswersSum = 0
peopleCount = 0


###########################################
#                 PART 2                  #
###########################################
def getEveryoneAnsweredQuestions():
    groupAnswersSum = 0
    for element in answeredQuestions.values():
        if element == peopleCount:
            groupAnswersSum += 1
    return groupAnswersSum


###########################################
#                 PART 1                  #
###########################################
for line in inputFile:
    line = line.split()

    if len(line) == 0:
        totalAnswersSum += len(answeredQuestions)
        everyoneAnswersSum += getEveryoneAnsweredQuestions()
        answeredQuestions.clear()
        peopleCount = 0
    else:
        peopleCount += 1
        for element in line[0]:
            if element not in answeredQuestions:
                answeredQuestions[element] = 1
            else: 
                answeredQuestions[element] = answeredQuestions[element] + 1



# Sums last line because it wans't detected
totalAnswersSum += len(answeredQuestions)
everyoneAnswersSum += getEveryoneAnsweredQuestions()

print("All answered questions: ", totalAnswersSum)
print("Questions that everyone answered: ", everyoneAnswersSum)