class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        prevmap = {}            # hashmap to check where the difference is stored 

        
        for i, n in enumerate(nums): 
            diff = target - n   
            if diff in prevmap: 
                return [prevmap[diff],i] 
            prevmap[n] = i 
