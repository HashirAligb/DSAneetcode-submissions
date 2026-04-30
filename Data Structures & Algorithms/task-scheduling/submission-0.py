class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #so i will use a maxheap and a queue, so that i can track the counts of a letter 
        # i have to also have a time variable and ill put that in my queue to see when i ca re add that to my max heap 
        # basically if the first val of my queues time is equal to the current time is ready to be readded to my maxheap 
        # also i have to add 1 to the count each time to basically decrement the count since i used it 


        count = Counter(tasks) #makes a hashmap for me with the counts as vals of each letter 
        q = deque()  
        maxheap = [-cnt for cnt in count.values()] 

        heapq.heapify(maxheap) 
        time = 0
        while maxheap or q: 
            time += 1   
          
            if maxheap:                 
                cnt = 1 + heapq.heappop(maxheap) 
                if cnt: 
                    q.append([cnt, time + n]) 
            if q and q[0][1] == time: 
                heapq.heappush(maxheap, q.popleft()[0]) 
        return time 
