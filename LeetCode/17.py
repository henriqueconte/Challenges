class Solution:
    def letterCombinations(self, digits):
        ans = []
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
        letters = []
        for digit in digits:
            letters.append(phoneDict[digit])

        self.combine_letters(letters, 0, "", ans)

        return ans

    def combine_letters(self, letters, index, curr_comb, ans):
        if index < len(letters):
            for letter in letters[index]:
                self.combine_letters(letters, index + 1, curr_comb + letter, ans)
                
        if len(curr_comb) == len(letters):
            ans.append(curr_comb)

solution = Solution()
print(solution.letterCombinations("23"))