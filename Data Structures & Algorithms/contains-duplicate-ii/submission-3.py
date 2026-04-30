class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # so i gotta check if theres atleast 2 nums that add up to <= k  
        window = set() 
        l = 0  

        for r in range(len(nums)): 
            if r - l > k: 
                window.remove(nums[l]) 
                l += 1  
            if nums[r] in window: 
                return True 
            window.add(nums[r]) 
        return False 