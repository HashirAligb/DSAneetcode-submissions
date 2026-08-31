class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[] for i in range((len(nums) + 1))] 
        

        count = {} 

        for i in nums: 
            count[i] = 1 + count.get(i, 0) 


        for key, val in count.items(): 
            res[val].append(key) 

    

        ans = [] 

        for i in range(len(res) -1, -1, -1): 
            for let in res[i]:
                ans.append(let)
                if len(ans) == k: 
                    return ans   
                   
                     

            
            



