class Solution:
    def longestPalindrome(self, s):
        letterDict = {}
        evenCount = 0
        longestOdd = 0
        hasOdd = 0

        for letter in s:
            if letter in letterDict:
                letterDict[letter] += 1
            else:
                letterDict[letter] = 1


        for element in letterDict.values():
            if element % 2 == 0:
                evenCount += element
            else:
                evenCount += element - 1
                hasOdd = 1
                longestOdd = max(longestOdd, element)
        
        return evenCount + hasOdd
    
anneExample = "anneivotemorecarsracerometovienna"
test = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
solution = Solution()
print(solution.longestPalindrome(test))

# aabbcdcbbaa