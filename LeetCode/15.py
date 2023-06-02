class Solution:
    def threeSum(self, nums):
        resultList = []
        nums = sorted(nums) # O(n log n)

        for i in range(len(nums)): 
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    resultList.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1

        return resultList
    
solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))
print(solution.threeSum([0,1,1]))
print(solution.threeSum([0,0,0]))

# -4, -1, -1, 0, 1, 2
# 