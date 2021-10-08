## Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = dict()
        for index, element in enumerate(nums):
            if f"{element}" in numsDict:
                numsDict[f"{element}"].append(index)
            else:
                numsDict[f"{element}"] = [index]
        
        for index, element in enumerate(nums):
            diff = f"{(target - element)}"
            if diff in numsDict:
                if target - element == element:
                    if len(numsDict[diff]) > 1:
                        return [
                            numsDict[f"{element}"][0],
                            numsDict[f"{element}"][1]
                        ]
                else:
                    return [
                        numsDict[f"{target - element}"][0], 
                        numsDict[f"{element}"][0]
                    ]