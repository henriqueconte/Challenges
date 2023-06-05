class Solution:
    def productExceptSelf(self, nums):
        result = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1] 

        right = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] = result[i] * right
            right = right * nums[i]
        return result
    
solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))


# [1,2,3,4,5,6,7,8,9]
# [1,1,2,6,24,120,720,5040,40320,362880]
# [0,0,0,0,0,0,0,0,362880]

        