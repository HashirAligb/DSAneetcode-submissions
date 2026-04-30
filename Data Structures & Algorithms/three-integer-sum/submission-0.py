class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:      
        # i have ot get the 3 unique elements that wll giveme a sum of 0  

        res = [] 
        nums.sort() 


        for i, z in enumerate(nums): 
            if z > 0: 
                break 
            if i > 0 and z == nums[i-1]:
                continue 
            l, r = i+1, len(nums) - 1 
            while l < r: 
                threeSum = z + nums[l] + nums[r] 
                if threeSum > 0: 
                    r -= 1 
                elif threeSum < 0: 
                    l += 1 
                else: 
                    res.append([z,nums[l], nums[r]]) 
                    l+= 1 
                    while nums[l] == nums[l-1] and l<r: 
                        l += 1 
        return res

    
        