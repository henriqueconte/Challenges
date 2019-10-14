def findLongest(word1, word2, s1, s2):
    
    for firstIndex in range(0,s1+1):
        for secondIndex in range(0,s2+1):
            if firstIndex == 0 or secondIndex == 0:
                valueTables[firstIndex][secondIndex] = 0
            elif word1[firstIndex-1] == word2[secondIndex-1]:
                valueTables[firstIndex][secondIndex] = valueTables[firstIndex-1][secondIndex-1] + 1
            else:
                valueTables[firstIndex][secondIndex] = max(valueTables[firstIndex-1][secondIndex], valueTables[firstIndex][secondIndex-1])

    print(valueTables[s1][s2])

while True:
    try:
        firstWord = input() 
        secondWord = input()
        size1 = len(firstWord)
        size2 = len(secondWord)

    except:
        break
            
    valueTables = [[0 for firstIndex in range(size2+1)]for secondIndex in range(size1+1)]

    findLongest(firstWord, secondWord, size1, size2)