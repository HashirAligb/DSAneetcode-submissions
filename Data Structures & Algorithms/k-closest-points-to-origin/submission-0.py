class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #for this I just neeed to use the fomula to get the distances and compare them 
        #then ill insert them into a minheap and return the k losest elements based off the distances 

        minheap = [] 

        for x, y in points: 
            dist = (x ** 2) + (y ** 2) 
            minheap.append([dist, x, y]) 
        
        heapq.heapify(minheap)  
        
        res = []

        # i dont wannna return my dist so il keep that out 
        while k > 0:  
            dist, x, y = heapq.heappop(minheap) 
            res.append([x,y]) 
            k -= 1 
        return res 
