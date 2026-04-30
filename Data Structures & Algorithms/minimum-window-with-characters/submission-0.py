class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return "" 
        wordT, wordS = {}, {} 

        for i in t: 
            wordT[i] = 1 + wordT.get(i,0)
        
        have, need = 0, len(wordT)  

        res = [-1,-1]
        resL = 10001 
        l = 0 

        for r in range(len(s)): 
            c = s[r] 
            wordS[c] = 1 + wordS.get(c,0) 

            if c in wordT and wordS[c] == wordT[c]:  
                have += 1 
            while have == need:  
                if (r-l) + 1 < resL: 
                    resL = (r-l) + 1   
                    res = [l,r]  
                wordS[s[l]] -= 1  
                if s[l] in wordT and wordS[s[l]] < wordT[s[l]]: 
                    have -= 1
                l += 1  
            
        l, r = res 

        return s[l:r+1] if resL != 1001 else ""

            
            


