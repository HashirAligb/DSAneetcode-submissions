class Solution:
    def longestPalindrome(self, s: str) -> str:
        # i want to search left right from the middle letter for optimal runtime 
        # ill do one while loop for even lenght string and one for odd 
        # this will ensure that i am able to do my twoo pointer approach for both 
        res = "" 
        sublength = 0 

        for i in range(len(s)):  
            # odd length case 
            l, r = i, i 
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if (r - l) + 1 > sublength: 
                    res = s[l: r+1] 
                    sublength = (r-l) + 1 #getting the distance 
                l -= 1 # going outward direction
                r += 1  
            
            # now I will handle the even string length case 
            l, r = i, i + 1 
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if (r - l) + 1 > sublength: 
                    res = s[l: r+1] 
                    sublength = (r-l) + 1
                l -= 1 
                r += 1  

        return res 
