class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # so ill initally keep track of my start inerval, after sorting ofc 
        # next ill compare the ending of my crurrent interval to my start  
        # if its withn the bounds of my start one then i need ot update my prevend pointer 
        # which was initally the end of my start interval to whatever the minumum end of both intervals 
        # is because essentially deleting the longer interval would be more efficient 
        # and the problem wants to know how many MINUMUM rekmovals it would take 
        # we dont need to actually remove so ill just update the ptr 


        intervals.sort() 
        prevend = intervals[0][1] 
        res = 0 
        for start, end in intervals[1:]:  
            if start >= prevend: 
                prevend = end  
            else:  
                res += 1  
                prevend = min(end, prevend) 
        return res 

                

            
