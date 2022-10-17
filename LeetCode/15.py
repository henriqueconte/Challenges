class Solution:
    def threeSum(self, nums):
        resultsSet = set()
        resultsList = []
        solutionsDict = dict()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j:
                    sumString = str(nums[i] + nums[j])
                    if sumString in solutionsDict:
                        solutionsDict[sumString].append((i,j))
                    else:
                        solutionsDict[str(nums[i] + nums[j])] = [(i,j)]

        for i in range(len(nums)):
            targetValue = str(0 - nums[i])
            try:
                tupleList = solutionsDict[targetValue]
                for tuple in tupleList:
                    if i != tuple[0] and i != tuple[1]:
                        solutionValuesList = [nums[tuple[0]], nums[tuple[1]], nums[i]]
                        solutionValuesList.sort()
                        stringSolution = str(solutionValuesList[0]) + "," + str(solutionValuesList[1]) + "," + str(solutionValuesList[2])

                        resultsSet.add(stringSolution)
        
            except KeyError:
                pass
                
        for element in resultsSet:
            stringList = element.split(",")
            intList = [eval(i) for i in stringList]
            resultsList.append(intList)
        print(resultsSet)
        return resultsList

    def find3Numbers(self, A, arr_size, sum):
        for i in range(0, arr_size-1):
            # Find pair in subarray A[i + 1..n-1]
            # with sum equal to sum - A[i]
            s = set()
            curr_sum = sum - A[i]
            for j in range(i + 1, arr_size):
                if (curr_sum - A[j]) in s:
                    print("Triplet is", A[i],
                            ", ", A[j], ", ", curr_sum-A[j])
                    return True
                s.add(A[j])
     
        return False

a = Solution()

a.threeSum([-1,0,1,2,-1,-4])
# a.find3Numbers([-1,0,1,2,-1,-4], len([-1,0,1,2,-1,-4]), 0)

    