import copy 

class Solution:
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)
        
        combinations = []

        def backtracking(candidates, target, currentSum, currentCandidates, currentIndex):
            if currentSum == target:
                combinations.append(currentCandidates)
            elif currentSum < target:
                for i in range(currentIndex, len(candidates)):
                    newCandidates = copy.deepcopy(currentCandidates)
                    newCandidates.append(candidates[i])
                    newSum = currentSum + candidates[i]
                    if newSum > target:
                        break
                    backtracking(candidates, target, newSum, newCandidates, i)

            return 
        
        backtracking(candidates, target, 0, [], 0)

        return combinations
        
    

        
solution = Solution()
print(solution.combinationSum([2,3,6,7], 7))
print(solution.combinationSum([2,3,5], 8))