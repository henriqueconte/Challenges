class Solution:
    def longestPalindrome(self, s):
        longest_pal = ""

        for i in range(len(s)):
            
            # Odd palindromes
            current_pal = self.palindrome_from_mid(s, i, i)
            if len(current_pal) > len(longest_pal):
                longest_pal = current_pal
        
            # Even palindromes
            current_pal = self.palindrome_from_mid(s, i, i+1)
            if len(current_pal) > len(longest_pal):
                longest_pal = current_pal

        return longest_pal
    
    def palindrome_from_mid(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

solution = Solution()
print(solution.longestPalindrome("baaab"))
print(solution.longestPalindrome("asdfbaaabdfd"))
print(solution.longestPalindrome("cbbd"))
print(solution.longestPalindrome("babad"))

# Solution: 
# Start from center and increase palindrome until it finds different characters
# Then, divide and conquer to find the biggest palindrome on the left and on the right side