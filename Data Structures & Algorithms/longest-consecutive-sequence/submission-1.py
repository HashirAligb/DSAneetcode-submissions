class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  
       answer = set(nums) 
       
       longest = 0 

       for i in answer: 
            if (i-1) not in answer: 
                length = 1  
                while (i + length) in answer:  
                    length += 1 
                longest = max(longest, length) 
       return longest 




