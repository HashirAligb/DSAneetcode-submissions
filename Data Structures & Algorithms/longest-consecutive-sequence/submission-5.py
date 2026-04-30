class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  
        seen = set(nums) 
        longest = 0 

        for i in nums: 
            if i - 1 not in seen: 
                start = 1 
                while i + start in seen: 
                    start += 1 
                longest = max(longest, start) 
        return longest 
        
