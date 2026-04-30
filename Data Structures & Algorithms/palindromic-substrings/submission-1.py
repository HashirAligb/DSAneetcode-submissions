class Solution:
    def countSubstrings(self, s: str) -> int:
       # ill count both ways using two ptrs and put that in a helper func  
       # then ill increment count for the even subtstr length iteration and odd length  
       # at the end ill return the total  
        res = 0 
        for i in range(len(s)):
            l = r = i 
            res += self.countpali(s,l,r) 
            l, r = i, i + 1 
            res += self.countpali(s, l, r)
        return res 
    def countpali(self, s, l, r): 
        res = 0 # local res to return back up 
        while l >= 0 and r < len(s) and s[l] == s[r]: 
            res += 1 
            l -= 1 
            r += 1  
        return res 
        
