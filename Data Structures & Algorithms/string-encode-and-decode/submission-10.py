class Solution:

    def encode(self, strs: List[str]) -> str: 
        new_str = ""
        for words in strs: 
            new_str += str(len(words))
            new_str += "#"  
            new_str += words 
        
        return new_str 
    
    

    def decode(self, s: str) -> List[str]:
        l = 0 

        j = ""
        r = 0
        res = []
        while r < len(s): 
            while s[r] != "#":    
                j += s[r] 
                r += 1
            l = r + 1
            r = l + int(j)  
            res.append(s[l:r])  
            j = ""
        return res
        

        

            

