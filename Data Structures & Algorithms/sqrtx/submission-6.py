class Solution:
    def mySqrt(self, x: int) -> int: 
        # ill binary search to be able to get the latest sqrt number  
        # or the actual one because it'll be logn time  
        # ill chekc middle first cast my res as middle in case we dont find 
        # and exact match in which case we return the greatest candidtate less than x 

        l, r = 0, x 
        res = 0
        while l <= r: 
            m = l + (r - l)// 2  
            if m * m > x: 
                r = m - 1 
            elif m * m < x:
                res = m 
                l = m + 1  
            else: 
                return m
        return res 
           


    