class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        freqmap = {} 

        for i in nums: 
            freqmap[i] = 1 + freqmap.get(i,0) 
        
        for i in freqmap: 
            if freqmap[i] == 1: 
                return i 
        