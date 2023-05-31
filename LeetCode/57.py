class Solution:
    def insert(self, intervals, newInterval):
        result = []
        left = newInterval[0]
        right = newInterval[1]
        isSearching = True

        for i in range(len(intervals)):
            if intervals[i][1] < left:
                result.append(intervals[i])
            elif intervals[i][0] > right:
                if isSearching:
                    result.append(newInterval)
                    isSearching = False
                result.append(intervals[i])
            elif isSearching:         # New interval start is contained on this interval
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(right, intervals[i][1])

        if not result or isSearching:
            result.append(newInterval)

        return result

solution = Solution()
print(solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(solution.insert([[1,3],[6,9]], [2,5]))
print(solution.insert([[1,3],[6,9]], [0,5]))
print(solution.insert([[1,3],[6,9]], [0,11]))
print(solution.insert([[1,3],[6,9]], [1,9]))