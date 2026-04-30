class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]  

        hashmap = Counter(nums)
        
        for n, c in hashmap.items():  
            freq[c].append(n)   
        
        res = []
        
        for i in range(len(freq) - 1, 0, -1):   
            for c in freq[i]: 
                if k == 0: 
                    return res  
                res.append(c)  
                if len(res) == k: 
                    return res 
    





        
            
                                