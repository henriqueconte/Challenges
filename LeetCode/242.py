import copy

class Solution:
    def isAnagram(self, s, t):
        sDict = {}
        tDict = {}

        for char in s:
            if char in sDict:
                sDict[char] += 1
            else:
                sDict[char] = 1

        for char in t:
            if char in tDict:
                tDict[char] += 1
            else:
                tDict[char] = 1

        sDictCopy = copy.deepcopy(sDict)
        for key, value in sDict.items():
            if key in tDict and value == tDict[key]:
                tDict.pop(key)
                sDictCopy.pop(key)

        return not tDict and not sDictCopy
    
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))
print(solution.isAnagram("ab", "a"))