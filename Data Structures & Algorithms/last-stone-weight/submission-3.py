class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # ill just use. min heap and silate it with negative values to act like a max heap 
        # next i will take my first max val and second ma val and have a condition to get the difference 
        # lastly ill just append whatevr difference i just got back in my simulated max heap 
        # also for the edge case of not having any vals left in my heap return 0  

        stone = [ -i for i in stones] 

        heapq.heapify(stone) 

        while len(stone) > 1: 
             first = heapq.heappop(stone) 
             second = heapq.heappop(stone) 
           
             if first != second:  
                heapq.heappush(stone, first - second) 

        return abs(stone[0]) if stone else 0  

