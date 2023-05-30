# Find first positive
# Keep adding until current Number > current Sum
# If current Number > current Sum,
# Reset current Sum with current Number

class Solution:
    def maxSubArray(self, nums):
        currentSum = 0
        highestSum = -inf

        for i in range(len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])
            highestSum = max(highestSum, currentSum)
            
        return highestSum
    
solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

