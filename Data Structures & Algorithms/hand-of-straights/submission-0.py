class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # solving with a minheap 
        # the minumum value should always be the start of a group 
        # so if its not the top of my minheap i can ret false 
        # also ill be usinfg a hasmap as a counter 
        # this way i can check if the neihboring numbers are available till the loop limit which is the group size 
        # last i can set a base case being if the len of the array is divisible by the group size in the first place 


        hashmap = {} 

        for i in hand: 
            hashmap[i] = 1 + hashmap.get(i, 0) 

        minh = list(hashmap.keys()) 
        heapq.heapify(minh) 

        while minh:  
            first = minh[0]
            for i in range(first, first + groupSize): 
                if i not in hashmap: # means theres a gap so a group cant be formed 
                    return False 
                
                hashmap[i] -= 1 

                if hashmap[i] == 0:  # so if the counter becomes 0 ill remove it
                    if i != minh[0]:    #so if i became - but it wasnt the smallest value we will have a gap in our groupsize
                         return False 
                    heapq.heappop(minh)
        return True 
                
            
                