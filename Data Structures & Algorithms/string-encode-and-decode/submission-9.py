class Solution:

    def encode(self, strs: List[str]) -> str:   
        res = ""
        for s in strs:  
            res += (str(len(s)) + "#" + s) 
        return res
        
    "2#we 3#say 1#: 3#yes"
    def decode(self, s: str) -> List[str]:  
        res = []

        i = 0 
        j = 0 
        while j < len(s): 
            digit = "" 

            while s[j] != "#":  
                j += 1 
            digit = s[i:j]  
          
            
            i = j + 1
            j = i + int(digit) 

            res.append(s[i: j])   
            i = j 

        return res 





            

