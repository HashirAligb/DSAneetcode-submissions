class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = [] 

        for n in nums: 
            if len(minheap) < k: 
                heapq.heappush(minheap, n) 
            else:  
                heapq.heappushpop(minheap, n) 
        
        return minheap[0] 
