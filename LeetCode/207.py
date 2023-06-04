class Solution:
    def canFinish(self, numCourses, prerequisites):
        if not prerequisites:
            return True
        
        if ((numCourses - 1) * numCourses) / 2 > len(prerequisites):
            return False

        requisitesDict = {}
        canFinishCourses = set()
        visited = set()
        foundCycle = False

        for element in prerequisites:
            course = str(element[0])
            requisite = str(element[1])

            if course in prerequisites:
                requisitesDict[course].append(requisite)
            else:
                requisitesDict[course] = [requisite]

        for course in requisitesDict:
            # if course in canFinishCourses:
            #     continue
            if self.validateCourse(course, visited, requisitesDict) == False:
                return False

        return True

    def validateCourse(self, course, visited, requisitesDict):
        if course not in requisitesDict:
            return True
        
        validatedCourse = True
        requisites = requisitesDict[course]
        for element in requisites:
            if element in visited:
                return False
            visited.add(element)
            validatedCourse = self.validateCourse(element, visited, requisitesDict)
        # if validatedCourse:

        return validatedCourse
        # if self.foundCycle == False:
        #     self.canFinishCourses.add(course)

solution = Solution()
# print(solution.canFinish(2, [[1,0]]))      
# print(solution.canFinish(2, [[1,0], [0,1]]))
# print(solution.canFinish(4, [[1,2], [2,3], [3,4]]))            
# print(solution.canFinish(2, [[0,1]]))  
print(solution.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))  

# [1, 2] -> [2, 1]
# [2, 3] -> [3, 2]
# [3, 1] -> [1, 3]
    
# 4 + 3 + 2 + 1
# 5 + 4 + 3 + 2 + 1
# 5 * (6) / 2 =

# [0,1] [0,2], [0,3], [0,4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3,4]

# Implementation 1:
# Sort pre requisits list based on pair[0]
# iterate over list, add course label to set after we finish reading pre requisits of a course
# if we try to read a pre requisit


# Implementation 2:
# Build graph with rules
# If find cycle on graph, return false


# 0 -> 1    -
# 1 -> 2, 3 -
# 2 -> 3   -
# 3 -> 4   -