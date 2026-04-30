class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #first case i want to handle is if my par is an open par 
        # ill just upd count 
        # and ill append to the res 
        # if my count is more than 0 that means I dont have closing par to match 
        # so whenevr theres a closing par i will decr count 
        # if its not a par then ill just update as normal 
        # ill use that same count var to remove the excess open par by going in reverse 
        # and removing the extra open then re reversing 

        res = [] 
        count = 0 
        for c in s: 
            if c == "(": 
                res.append(c) 
                count += 1 
            elif c == ")" and count > 0: #i wont decr count if count is less ill just skip the closed par
                res.append(c) 
                count -= 1 
            elif c != ")": 
                res.append(c)  
        
        newres = [] 

        for i in res[::-1]: 
            if i == "(" and count > 0: 
                count -= 1 
            else: 
                newres.append(i) 
        
        return "".join(newres[::-1]) 
