import copy 

class Solution:
    def permute(self, nums):
        permutations = []

        def backtrack(nums, curr_index):
            if curr_index == len(nums):
                nums_copy = copy.copy(nums)
                permutations.append(nums_copy)
            else:
                for i in range(curr_index, len(nums)):
                    nums[i], nums[curr_index] = nums[curr_index], nums[i]
                    backtrack(nums, curr_index + 1)
                    nums[i], nums[curr_index] = nums[curr_index], nums[i]
             
        backtrack(nums, 0)

        return permutations
    
solution = Solution()
print(solution.permute([1,2,3]))
print(solution.permute([0,1]))
print(solution.permute([1]))