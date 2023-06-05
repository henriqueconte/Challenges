class Solution:
    def productExceptSelf(self, nums):
        result = [0 for _ in range(len(nums))]
        leftProduct = [1 for _ in range(len(nums))]
        rightProduct = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            leftProduct[i] = nums[i-1] * leftProduct[i-1]

        for i in range(len(nums) -2, -1, -1):
            rightProduct[i] = nums[i+1] * rightProduct[i+1]

        for i in range(len(nums)):
            result[i] = leftProduct[i] * rightProduct[i]

        return result
    
solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))


        