class Solution:
    def addBinary(self, a, b):
        smallerNum = min(a, b)
        i = len(smallerNum)
        newNumber = ""
        carrier = 0

        while i != 0:
            i -= 1
            currentDigit = int(a[i]) + int(b[i]) + carrier
            print(currentDigit)
            if currentDigit == 0 or currentDigit == 1:
                newNumber = "".join([str(currentDigit), newNumber]) 
                carrier = 0
            elif currentDigit == 2:
                print("before" , newNumber)
                newNumber = "".join(["0", newNumber])
                print("after ", newNumber)
                carrier = 1
            elif currentDigit == 3:
                newNumber = "".join(["1", newNumber])
                carrier = 1

        return newNumber


#   1 0 1 0
#   1 0 1 1
# 1 0 1 0 1

solution = Solution()
print(solution.addBinary("11", "1"))