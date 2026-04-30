class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for i in range(len(nums)+1)]     # first we make the list of lists to create our bucket sort 
        count = {}                                  # we create a map to hold how many times each number appears 

        for n in nums:                              # loop through the array 
            count[n] = 1 + count.get(n,0)         # get its current count add 1 to it if none return 0 
        for n, c in count.items():                           # now we assign the value to the index(basically how many times it showed up)
            freq[c].append(n)

        res = []                                     #now we create the result list

        for i in range(len(freq)-1, 0, -1):       #we decrement start dfrom the last index of the array go to 1 
            for n in freq[i]:                #we gotta get the value stored at the index of it cuz rm thats the count of the value
                res.append(n)   
                if len(res) == k:  
                    return res

        
            
                                