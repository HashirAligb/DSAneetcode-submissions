class Solution:
    def isValid(self, s: str) -> bool:

        # 
        closeMap = { ")" : "(", "}" : "{", "]" : "[" }
        stack = []  

        for i in s: 
            if i in closeMap:   
                if not stack: 
                    return False 

                if stack[-1] != closeMap[i]: 
                    return False   
                else: 
                    stack.pop() 
                    
            else:  
                stack.append(i) 
        
        if stack: 
            return False 
        return True 





        

                
            
                



        
        