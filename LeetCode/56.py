class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals)
        merged_intervals = [intervals[0]]
        
        for curr_interval in intervals:
             merged_intervals = self.merge_interval(merged_intervals, curr_interval)

        return merged_intervals
    
    def merge_interval(self, merged_intervals, curr_interval):
            if merged_intervals[-1][1] >= curr_interval[0]:
                 merged_intervals[-1][1] = max(merged_intervals[-1][1], curr_interval[1])
            else:
                merged_intervals.append(curr_interval)
            return merged_intervals
    
solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))
print(solution.merge([[1,4],[4,5]]))
            
            