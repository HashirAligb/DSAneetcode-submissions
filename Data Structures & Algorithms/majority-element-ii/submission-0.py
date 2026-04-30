class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        rounded = math.floor(len(nums) // 3) 

        hashmap = {}

        for i in nums: 
            hashmap[i] = 1 + hashmap.get(i,0) 
        
        res = []
        for i, k in hashmap.items(): 
            if k > rounded: 
                res.append(i) 
        return res 
