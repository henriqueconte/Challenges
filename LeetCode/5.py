class Solution:
    def longestPalindrome(self, s):
        longestPal = ""
        for i in range(len(s)):
            currentPal = self.palindromeFromCentre(s, i, i)
            if len(currentPal) > len(longestPal):
                longestPal = currentPal

            currentPal = self.palindromeFromCentre(s, i, i + 1)
            if len(currentPal) > len(longestPal):
                longestPal = currentPal

        return longestPal

    def palindromeFromCentre(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
        

a = Solution()
print(a.longestPalindrome("akka"))

#akka
#deified