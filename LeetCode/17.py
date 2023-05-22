class Solution:
    def letterCombinations(self, digits):
        # Circular buffer approach
        # offset = 0
        # Iterate over digits:
            # For every digit:
                # Loop on the characters of the digit, starting from 0 + offset (ex: if offset = 1 and digit = 3, start on E.)
                # If currentCharCount > len(charsDigit)
                    # currenctCharCount = 0

        # What if you brute force?

        offset = 0
        resultSize = 0
        phoneDict = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        resultCount = 0

        if len(digits) > 0:
            resultSize = 1
            for digit in digits:
                resultSize = resultSize * (len(phoneDict[digit]))

        result = ["" for x in range(resultSize)]

        # ad be cf    a b c   a b c

        for digit in digits:
            digitLetters = phoneDict[digit]
            for k in range(int(resultSize / len(digitLetters))):
                for i in range(len(digitLetters)): 
                 # Each digit is going to appear that amount of times
                    result[resultCount] += digitLetters[(i + (k * offset)) % len(digitLetters)] # Iterate over the digits to do like "a b c a b c"
                    resultCount += 1
                    # print(resultCount)
            offset += 1
            resultCount = 0

        return result

solution = Solution()

print(solution.letterCombinations("27"))     