from operator import le
from re import L


class Solution:
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        longSubstringCount = 0
        left = right = 0

        while (right < len(s)):
            if s[right] in charSet:
                if len(charSet) > longSubstringCount:
                    longSubstringCount = len(charSet)
                while s[left] != s[right]:
                    charSet.remove(s[left])
                    left += 1
                charSet.remove(s[left])
                left += 1
            else:
                charSet.add(s[right])
                right += 1


        return max(longSubstringCount, len(charSet))
        
a = Solution()

print(a.lengthOfLongestSubstring("pwwkew"))

## Examples: 

# p
# pw
# pww
# w
# wk
# wke
# wkekot