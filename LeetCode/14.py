class Solution:
    def longestCommonPrefix(self, strs):
        longestCommonPrefix = ""
        currentIndex = 0
        shortestStringSize = 999999999999
        for element in strs:
            shortestStringSize = min(shortestStringSize, len(element))
        
        while currentIndex < shortestStringSize:
            if self.hasSameLetter(strs, currentIndex):
                longestCommonPrefix += strs[0][currentIndex]
            else:
                return longestCommonPrefix
            currentIndex += 1

        return longestCommonPrefix
    
    def hasSameLetter(self, strs, index):
        for i in range(len(strs) - 1):
            if strs[i][index] != strs[i+1][index]:
                return False
        return True

a = Solution()

print(a.longestCommonPrefix(["dog","racecar","car"]))