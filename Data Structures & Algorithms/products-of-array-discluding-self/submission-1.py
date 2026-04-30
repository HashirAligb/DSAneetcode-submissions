class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums) 

        prefix = 1 
        for i in range(len(nums)): 
            res[i] = prefix         #we wanna just store our prefix for the first int 
            prefix *= nums[i]   #update our prefix by multiplying to store for he next slot 

        postfix = 1 
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix  #now we decrement an the last slot will just be multiplying 1 
            postfix *= nums[i]  #then we have to update the postfix by multipling it by the slot for the previous slot to store it
        return res 
