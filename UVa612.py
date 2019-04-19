dataSets = input()


blank = False

def countLetters (arrayDNA):
    copia = arrayDNA
    mudancas = 0
    for a in range(0, len(arrayDNA)):
        for b in range(a + 1, len(arrayDNA)):
            if arrayDNA[a] > arrayDNA[b]:
                mudancas = mudancas + 1

             
    return mudancas


def DNASort ( DNABase, DNAOrder):
    for i in range(1, len(DNABase)):
        currentNumber = DNAOrder[i]
        currentDNA = DNABase[i]
        while i > 0 and DNAOrder[i-1] > currentNumber:
            DNAOrder[i] = DNAOrder[i-1]
            DNABase[i] = DNABase[i-1]
            i = i-1
            DNAOrder[i] = currentNumber
            DNABase[i] = currentDNA
            
    return DNABase
    
for i in range(0, int(dataSets)):
    actualDataSet = []
    numberDataSet = []
    a = input()
    stringLength,stringNumber = input().split()

    for cont in range(0, int(stringNumber)):
        actualDataSet.append(input())
        number = countLetters(actualDataSet[cont])
        numberDataSet.append(number)
        
    actualDataSet = DNASort(actualDataSet, numberDataSet)
    
    if blank == True:
        print("")
    blank = True
    
    for cont in range(0, len(actualDataSet)):
        print(actualDataSet[cont])
    

    
"Hi,"

"This is an automated response from UVa Online Judge."

"Your submission with number 23124536 for the problem 612 - DNA Sorting has received the verdict Accepted."

"Congratulations! Now it is time to try a new problem."

"Best regards,"

"The UVa Online Judge team"     