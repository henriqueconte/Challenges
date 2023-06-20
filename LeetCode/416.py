class Solution:
    def canPartition(self, nums) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target = total_sum / 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            new_dp = set()
            for j in dp:
                new_dp.add(j)
                new_dp.add(nums[i] + j)
            dp = new_dp
    
solution = Solution()
# print(solution.canPartition([1,5,11,5]))
# print(solution.canPartition([1,2,3,5]))
print(solution.canPartition([2,2,1,1]))

# Sort array
# Begin pointer, end pointer
# If sum_begin < sum_end:

# [1, 5, 5, 5, 7]
# 

# [2, 8, 3, 1]

# 0, 2, 8, 10, 3, 5, 11, 13