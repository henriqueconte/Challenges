import math

class Solution:
    def kClosest(self, points, k):
        distanceList = []
        
        for point in points:
            distance = math.sqrt(math.pow(point[0],2) + math.pow(point[1],2))
            distanceList.append((distance, point))

        distanceList.sort()
        distanceList = distanceList[:k]
        resultList = []
        for element in distanceList:
            resultList.append(element[1])

        return resultList

solution = Solution()
print(solution.kClosest([[1,3],[-2,2]], 1))
print(solution.kClosest([[3,3],[5,-1],[-2,4]], 2))
    
