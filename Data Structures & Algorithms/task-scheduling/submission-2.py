class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # q to park my re apper times 
        # maxheap to track freqs 
        # countmap to generate freqs 

        countmap = Counter(tasks) 

        maxheap = [ -n for n in countmap.values()]    
        heapq.heapify(maxheap)
        time = 0  
        q = deque()

        while q or maxheap:  
            time += 1  
            if maxheap:  
                    cnt = 1 + heapq.heappop(maxheap)  
                    if cnt: 
                        q.append([cnt, time + n]) 
                
            if q and q[0][1] == time: 
                heapq.heappush(maxheap, q.popleft()[0])   

        return time 

                
