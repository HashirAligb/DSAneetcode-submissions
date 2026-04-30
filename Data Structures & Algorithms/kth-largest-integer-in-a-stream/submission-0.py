class KthLargest:
    #okay so off the bat i know that if i use a heap i can just get the kth largest element 
    # by pooping from it and the way i can make sure is by setting a statement for my heap to be 
    # less than or eual to the size of k if its not i wont pop so whether or not I add, itll handle the  
    # the size issue for me

    def __init__(self, k: int, nums: List[int]):
        self.minheap, self.k = nums, k 
        heapq.heapify(self.minheap) 

        while len(self.minheap) > k: 
            heapq.heappop(self.minheap) 

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val) 
        while len(self.minheap) > self.k: 
            heapq.heappop(self.minheap) 
        return self.minheap[0] 

