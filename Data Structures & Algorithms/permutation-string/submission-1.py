class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        
        z1, z2 = len(s1), len(s2) 

        if z1 > z2: return False 
    
        counts_s1 = [0] * 26 
        counts_s2 = [0] * 26  

        for i in range(z1):  
            counts_s1[ord(s1[i]) - 97] += 1 
            counts_s2[ord(s2[i]) - 97] += 1 
        
        if counts_s1 == counts_s2: return True 

        for i in range(z1, z2):  
            counts_s2[ord(s2[i]) - 97] += 1  
            counts_s2[ord(s2[i - z1]) - 97] -= 1 

            if counts_s1 == counts_s2: return True 
        
        return False 
 


            


        
   

        
        

                
            