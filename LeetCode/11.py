from operator import le
import copy

class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        biggestContainer = 0

        while left < right:
            biggestContainer = max(biggestContainer, (right - left) * min(height[left], height[right]))
            
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        
        return biggestContainer
        
        
                
a = Solution()
# print(a.maxArea([1,8,6,2,5,4,8,3,7]))
# print(a.maxArea([1,2,4,3]))
print(a.maxArea([2,3,10,5,7,8,9]))