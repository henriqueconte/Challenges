class Solution:
    def search(self, nums, target):
        pivot = self.find_pivot(nums, 0, len(nums) // 2)
        left_search = self.binary_search(nums, target, 0, pivot - 1)
        right_search = self.binary_search(nums, target, pivot, len(nums) - 1)

        if left_search == -1 and right_search == -1:
            return -1
        elif left_search != -1:
            return left_search
        else:
            return right_search
    
    def find_pivot(self, nums, left, right):
        if right == 0:
            return right
        if left == len(nums) - 1:
            return left
        if nums[right - 1] > nums[right]:
            return right

        if nums[left] > nums[right]: # is already pivoted
            return self.find_pivot(nums, left, (left + right) // 2)
        else:
            return self.find_pivot(nums, right, (right + len(nums)) // 2)

    
    def binary_search(self, nums, target, left, right):
        if right >= left:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.binary_search(nums, target, left, mid-1)
            else:
                return self.binary_search(nums, target, mid+1, right)
        else:
            return -1
    
solution = Solution()

# Idea: 
# Find pivoted index
# Run binary search again on left side and right of nums

print(solution.search([4,5,6,7,0,1,2], 0))
print(solution.search([4,5,6,7,0,1,2], 3))
print(solution.search([1], 0))