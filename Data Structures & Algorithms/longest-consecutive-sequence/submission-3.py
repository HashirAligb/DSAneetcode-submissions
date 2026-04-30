class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  

        seen = set(nums) 
        longest = 0   

        for i in nums: 
            if (i - 1) not in seen: 
                length = 1 
                while (i + length) in seen: 
                     length += 1 
                longest = max(longest, length) 
        return longest  
                  
            
