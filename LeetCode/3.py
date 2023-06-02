class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftPointer = 0
        rightPointer = 0
        maxSubstringCount = 0
        lettersSet = set()

        for letter in s:
            if letter in lettersSet:
                while letter != s[leftPointer]:
                    lettersSet.remove(s[leftPointer])
                    leftPointer += 1
                leftPointer += 1
            else:
                lettersSet.add(letter)
                rightPointer += 1
                maxSubstringCount = max(maxSubstringCount, len(lettersSet))

        return maxSubstringCount