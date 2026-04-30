class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0 

        for n in nums: 
            tmp = max(rob1 + n, rob2) 
            rob1 = rob2 
            rob2 = tmp 
            
        return rob2 



        # simulated : [rob1, rob2, n] 

        # you cant get rob2 with n so we will chose the max between rob1 + n, or just rob2  
        # in the end of the loop rob2 will eventually become, the last element and we will get either the max being n + rob1 or just rob2