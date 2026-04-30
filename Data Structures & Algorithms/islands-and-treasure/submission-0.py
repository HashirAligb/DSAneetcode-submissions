class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # im gonna do bfs from my two gates 
        # ill hodl a distance as a counter 
        # and ill save my distance in the grid at r, c 
        # the way thisll work is ill use a queue to hold my two gates first 
        # then ill check all 4 neighboring points of my two gates and just keep 
        # updating my distance since all i gotta do is modify in place 

        rows, cols = len(grid), len(grid[0])
        visited = set()  
        q = deque()  

        def addpt(r,c): 
            if (r < 0 or c < 0 or 
            r >= rows or c >= cols or 
            (r,c) in visited or 
            grid[r][c] == - 1):
                return  
            visited.add((r,c)) 
            q.append([r,c]) 

        for r in range(rows): 
            for c in range(cols):  
                if grid[r][c] == 0: 
                    q.append([r,c]) 
                    visited.add((r,c))  
        
        dist = 0
        while q:  
            for i in range(len(q)): 
                r, c = q.popleft()  #save the pts 
                grid[r][c] = dist #this where i update the relative distance  
                addpt(r + 1, c)
                addpt(r - 1, c) 
                addpt(r, c + 1) 
                addpt(r, c - 1) 
            dist += 1 
        

