class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = {0: 0, 1:0, 2:0} 

        for i in nums: 
            hashmap[i] = 1 + hashmap.get(i, 0)     

        i = 0
        while i < len(nums): 
            while hashmap[0] != 0: 
                nums[i] = 0  
                hashmap[0] -= 1 
                i += 1  
            while hashmap[1] != 0: 
                nums[i] = 1 
                hashmap[1] -= 1  
                i += 1 
            while hashmap[2] != 0: 
                nums[i] = 2 
                hashmap[2] -= 1 
                i += 1 
        return nums
          