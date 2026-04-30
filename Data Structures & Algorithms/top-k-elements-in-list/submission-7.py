from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

# so I'm finding nums that at least show up k times
# I can use a hahsmap to count the count
# then check the val w k 
# if val >= k, then return the keys of those vals in a list 
        count = Counter(nums)
        res = [item for item,freq in count.most_common(k)]

        return res

        


    
        

            
            
            


            