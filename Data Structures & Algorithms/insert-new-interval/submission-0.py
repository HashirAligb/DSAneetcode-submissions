class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # so ill handle three cases #1 is if my new intervals last part is less than  
        # the beginning of the next interval, ill just add it to the res then add the rest 
        # next ill see if the new intervals beginning is after the current intervals end, ill  
        # then add my current interval to my res 
        # last ill know that theres a merge required so ill take the min and max of the beginning 
        # and the end of my current interval and my new interval 

        res = [] 

        for i in range(len(intervals)): 
            if newInterval[1] < intervals[i][0]: 
                res.append(newInterval) 
                return res + intervals[i:]  # add everything that follows 
            elif newInterval[0] > intervals[i][1]: 
                res.append(intervals[i]) 
            else: 
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])] 
        
        # im gonna append the new interval outside my loop because it may potentially merge 
        # with other intervals in my loop 

        res.append(newInterval) 
        return res 