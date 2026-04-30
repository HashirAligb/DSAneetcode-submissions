class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0   
        total = 0 
        subarr = float('inf')

        for r in range(len(nums)):   
            total += nums[r]
            while total >= target: 
                subarr = min(subarr, r - l + 1) 
                total -= nums[l] 
                l += 1 
        return subarr if subarr != float('inf') else 0 
                        
            