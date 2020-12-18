class PlaneSeat:
    def __init__(self, seatCode):
        rowSum = 0
        columnSum = 0

        for i in range(0,7):
            if seatCode[i] == "B":
                rowSum += pow(2, 7 - i - 1)

        for i in range(7, 10):
            if seatCode[i] == "R":
                columnSum += pow(2, 10 - i - 1)

        self.rowSum = rowSum
        self.columnSum = columnSum
        self.seatID = (rowSum * 8) + columnSum

def getSeatID(seat):
    return seat.seatID

inputFile = open("inputs/Day5Input.txt")
highestSeatID = -1
planeSeatList = []
mySeatId = -1

###########################################
#                 PART 1                  #
###########################################
for line in inputFile:
    seatLine = line.split()[0]
    newPlaneSeat = PlaneSeat(seatLine)

    if newPlaneSeat.seatID > highestSeatID:
        highestSeatID = newPlaneSeat.seatID

    planeSeatList.append(newPlaneSeat)


###########################################
#                 PART 2                  #
###########################################
planeSeatList.sort(key=getSeatID)
for i in range (0, len(planeSeatList)):
    if i < len(planeSeatList) - 1:
        if planeSeatList[i].seatID + 1 != planeSeatList[i + 1].seatID:
            mySeatId = planeSeatList[i].seatID + 1

print("Highest seat ID:", highestSeatID)
print("My seat ID: ", mySeatId)