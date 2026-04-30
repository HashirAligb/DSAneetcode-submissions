class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        # we include nums[0] for the edge case of nums only having one variable 

    def helper(self, nums): 
        rob1, rob2 = 0, 0 

        for n in nums: 
            temp = max(rob1 + n, rob2) 
            rob1 = rob2 
            rob2 = temp 

        return rob2  

    # very simple coninuation of the first version, all we gotta do is turn the first versions 
    # solution into a helper function and call it on the subarray consisting of everyhting but the first index 
    # then everything but the last index 
    # returning its max and thats how we beat the problems catching edge case of the wrap around 
