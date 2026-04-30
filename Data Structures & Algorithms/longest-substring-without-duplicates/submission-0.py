class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #so this is gonna have a left and right ptr 
        #we will compare to see if they are the same 
        # if the right = the left  
       l = 0 
       maxS = 0  
       dup = set()

       for r in range(len(s)): 
            while s[r] in dup: 
                dup.remove(s[l]) 
                l += 1  
            dup.add(s[r]) 
            maxS = max(maxS, r - l + 1) 
       return maxS 
