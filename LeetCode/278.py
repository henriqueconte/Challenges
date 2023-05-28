# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n):
        mid = int(n / 2)
        
        while True:
            # print(mid)
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    # print("Found!")
                    break
                else:
                    mid = int(mid / 2)
            else:
                mid = int((mid + n) / 2)
            
        return mid
    
solution = Solution()

print(solution.firstBadVersion(4))


# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10