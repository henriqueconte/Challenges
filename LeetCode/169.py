class Solution:
    def majorityElement(self, nums):
        majorityElement = nums[0]
        majorityCount = 1
        for element in nums:
            if element == majorityElement:
                majorityCount += 1
            else:
                majorityCount -= 1
                if majorityCount == 0:
                    majorityElement = element
                    majorityCount += 1
                     
        return majorityElement
    
solution = Solution()
print(solution.majorityElement([3,2,3,2,2,3,2]))