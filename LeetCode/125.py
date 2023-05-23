import re

class Solution:
    def isPalindrome(self, s):
        regex = re.compile('[^a-zA-Z0-9]')
        s = regex.sub('', s)
        s = s.lower()
        left = 0
        right = len(s) - 1

        while (left <= right):
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
    
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("0P"))