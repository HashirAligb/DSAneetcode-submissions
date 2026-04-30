class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # im going to use a hashmap where ill track where the last indices of each letter is at 
        # the final index of where a letter is at is essentially how my window partion will be simulated 
        # also this is updated as we loop through our string bc im the window needs a start obv 
        # okay so ill compare each letters ending index and set my end to the max between the two 
        # then when my i reaches the end itself ill set my size var to 0 and append the size to my result before i set it to 0 
        # once thats all said and done i can return my final result 

        lastidx = {} 

        for i, n in enumerate(s): 
            lastidx[n] = i # this will keep re rendering so itll eventually get the last occurrence. 
        
        res = []
        end, size = 0, 0  
        for i, n in enumerate(s):   
            size += 1
            end = max(end, lastidx[n])  
            if i == end:  
                res.append(size) 
                size = 0  
        return res 


