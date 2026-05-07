class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket = [ [] for i in range(len(nums) + 1) ]  

        freqMap = Counter(nums) 


        for key, val in freqMap.items():  
            bucket[val].append(key) 
        

        res = []
        for i in range(len(bucket) - 1, -1, -1):  
            for w in bucket[i][::-1]: 
                if len(res) < k: 
                    res.append(w) 
        return res 

