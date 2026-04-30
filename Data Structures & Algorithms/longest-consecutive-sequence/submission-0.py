class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  
        
        answer = set(nums)
        longest = 0 

        for n in nums: 
            if (n-1) not in answer: 
                seq = 1
                while (n+seq) in answer: 
                    seq += 1 
                longest = max(seq,longest) 
        return longest 