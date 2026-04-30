class Solution:
    def jump(self, nums: List[int]) -> int:
        #okay so i will simulate a window, this window will also comapare 
        # my ptr next to i and my ptr from i + i's jumps 
        # ill set whatevers the max to farthest and thatll become my right ptr 
        # this way, ill keep looping through my left to right ptr comparing 
        # how far ill get if i jump to the box next to i or from i to its farthest  
        # jump and it even covers the boxes between whil keeping track of my jumps 

        res = 0 
        l = r = 0 

        while r < len(nums) - 1: # while we arent at my last index  
            farthest = 0  
            for i in range(l, r + 1):  
                farthest = max(farthest, i + nums[i]) # will keep updating getting us to our furthest box  
            
            l = r + 1 
            r = farthest  
            res += 1 
        return res 
             
            


    


                  

                
            
                
                




