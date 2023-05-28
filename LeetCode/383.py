class Solution:
    def canConstruct(self, ransomNote, magazine):
        ransomDict = {}
        
        for letter in ransomNote:
            if letter in ransomDict:
                ransomDict[letter] += 1
            else:
                ransomDict[letter] = 1

        for letter in magazine:
            if letter in ransomDict:
                ransomDict[letter] -= 1

        for element in ransomDict.values():
            if element > 0:
                return False

        return True
    
solution = Solution()
print(solution.canConstruct("a", "b"))