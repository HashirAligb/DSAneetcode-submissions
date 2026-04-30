class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # so I will set up a cursum and maxsum 
        # my cursum however will reset to 0, if my value makes it become negative 
        # this will simulate a new subarray which can generate us a new cur sum and i will then 
        # compare it with maxsum and update whichever is larger  
        # at the end of my loop the maxsum should be the max subarry sum so i can return and its O(N) 

        maxSum = nums[0]  
        curSum = 0  

        if len(nums) == 1: 
            if nums[0] < 0: 
                return nums[0]  

        for i in range(len(nums)):  
            curSum = max(curSum, 0) 
            curSum += nums[i]  
            maxSum = max(maxSum, curSum) 
        
        return maxSum 


            
