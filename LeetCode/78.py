class Solution:
    def subsets(self, nums):
        ans = []
        self.backtrack(nums, [], ans, 0)
        return ans                


    def backtrack(self, nums, temp_list, ans, start):
        ans.append(temp_list)
        print(temp_list)
        for i in range(start, len(nums)):
            self.backtrack(nums, temp_list+[nums[i]], ans, i+1)
    
solution = Solution()

print(solution.subsets([1,2,3]))
# print(solution.subsets([0]))