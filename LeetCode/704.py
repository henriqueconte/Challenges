class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while (left <= right):
            index = (left + right) // 2
            if nums[index] == target:
                return index
            elif nums[index] > target:
                right = index - 1
                index = int(index / 2)
            else:
                left = index + 1
                index = int((index + len(nums)) / 2)
                
        return -1
    
solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], 12))