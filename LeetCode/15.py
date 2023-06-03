class Solution:
    def threeSum(self, nums):
        resultList = []
        tripletsSet = set()
        nums = sorted(nums) # O(n log n)

        for i in range(len(nums)): 
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    tripletsSet.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1

        for triplet in tripletsSet:
            resultList.append([triplet[0], triplet[1], triplet[2]])
        return resultList
    
solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))
print(solution.threeSum([0,1,1]))
print(solution.threeSum([0,0,0]))

# -4, -1, -1, 0, 1, 2
# 