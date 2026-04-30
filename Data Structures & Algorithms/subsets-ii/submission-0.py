class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # gonna sort to be able to use my while loop to skip duplicate numbers 
        # ill call dfs initially WITH my number t i included then ill pop 
        # and have my while loop set up to be able to handle the duplicate numbers 
        # and also make sure i = 1 is in bounds 
        # ill call dfs again after my while loop to be able to get a distinct subset that doesnt have  
        # the i so that my res only contains distinct subsets 


        nums.sort() 
        res = [] 

        def dfs(i, subset): 
            if i == len(nums): # basically when our ptr reaches the end each call 
                res.append(subset[::]) # adds a COPY of subset since subset is a reference thats interchangeable
                return 
            
            subset.append(nums[i])
            dfs(i + 1, subset) 
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]: 
                i += 1 
            
            dfs(i + 1, subset)    
        dfs(0, [])
        
        return res 
