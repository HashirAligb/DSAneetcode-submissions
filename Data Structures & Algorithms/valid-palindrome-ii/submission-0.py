class Solution:
    def validPalindrome(self, s: str) -> bool:
        # create my ptrs 
        # gitta return false if not pal but check my two cases  
        # two cases would be whether or not the thing is pal if del left or 
        #del the right
        
        l, r = 0, len(s) - 1  

        while l < r:  
            if s[l] != s[r]: 
                eraseL, eraseR = s[l+1: r+1], s[l:r] 
                return (eraseL == eraseL[::-1] or eraseR == eraseR[::-1]) 
            l, r = l + 1, r - 1 
        return True 
