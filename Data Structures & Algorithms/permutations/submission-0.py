class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # im basically gonna have a tree in theory where i get combinations of all my numbers after the first index 
        # thats gonna be a recursive call tho^, so ill eventually have an empty subset 
        # since itll climb back wiht multiple subsets, when i finish, ill finally add my very first element to the diff 
        # generated subsets 

        if len(nums) == 0: 
            return [[]] 
        
        perms = self.permute(nums[1:]) 
        res = [] 

        for p in perms: 
            for i in range(len(p) + 1):  # my loop to insert i at all the diff indices
                p_copy = p.copy() 
                p_copy.insert(i, nums[0]) 
                res.append(p_copy) 
        return res 
