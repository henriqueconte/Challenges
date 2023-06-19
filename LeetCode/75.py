class Solution:
    def sortColors(self, nums) -> None:
        colors_dict = {
            "0": 0,
            "1": 0,
            "2": 0
            }

        for num in nums:
            colors_dict[str(num)] += 1     
    
        for i in range(0, colors_dict["0"]):
            nums[i] = 0

        for i in range(colors_dict["0"], colors_dict["0"] + colors_dict["1"]):
            nums[i] = 1

        for i in range(colors_dict["0"] + colors_dict["1"], colors_dict["0"] + colors_dict["1"] + colors_dict["2"]):
            nums[i] = 2

        # print(nums)
        # for i in range(len(nums))
        """
        Do not return anything, modify nums in-place instead.
        """

solution = Solution()
solution.sortColors([2,0,2,1,1,0])
# print(solution.sortColors([2,0,1]))