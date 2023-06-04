class Solution:
    def canFinish(self, numCourses, prerequisites):
        if not prerequisites:
            return True
        
        maxAmountOfPrerequisites = ((numCourses - 1) * numCourses) / 2
        if len(prerequisites) > maxAmountOfPrerequisites:
            return False
        
        requisitesDict = {}

        for element in prerequisites:
            course = str(element[0])
            requisite = str(element[1])

            if course in requisitesDict:
                requisitesDict[course].append(requisite)
            else:
                requisitesDict[course] = [requisite]

        approvedCourses = set()
        analysingCourses = set()
        def hasCycle(course):
            if course in approvedCourses:
                return False
            elif course in analysingCourses:
                return True
            elif course not in requisitesDict:
                approvedCourses.add(course)
                return False
            
            analysingCourses.add(course)

            for requisite in requisitesDict[course]:
                if hasCycle(requisite):
                    return True

            analysingCourses.remove(course)
            approvedCourses.add(course)

            return False
        
        for course in requisitesDict:
            if hasCycle(course):
                return False
            
        return True



solution = Solution()
print(solution.canFinish(2, [[1,0]]))      
print(solution.canFinish(2, [[1,0], [0,1]]))
print(solution.canFinish(4, [[1,2], [2,3], [3,4]]))            
print(solution.canFinish(2, [[0,1]]))  
print(solution.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))  
print(solution.canFinish(3, [[1,0],[1,2],[0,1]])) 
print(solution.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]] )) 
print(solution.canFinish(8,[[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]] )) 

# 1 -> 4
# 2 -> 4
# 3 -> 1
# 3 -> 2