class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]  
        res = []

        
        cntmap = Counter(nums) 

        for key, val in cntmap.items(): 
            bucket[val].append(key)
        
        for box in range(len(bucket) -1, 0, -1): 
            for i in bucket[box]:  
                if len(res) == k: 
                    return res 
                else: 
                    res.append(i) 
        return res 
        