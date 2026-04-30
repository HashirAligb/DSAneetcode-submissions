class Solution:
    def checkValidString(self, s: str) -> bool:
        # im gonna use a left min and and a left max to create a rangeforme  
        # this range will represent all the different possibilities through my iteration 
        # if my leftmin ever falls under 0 i can set it back up to 0 to represent and empty case for * 
        # thats how ill handle the * case where we have multiple possibilities otherwise ill just increment accordingly 
        # in the end ill return true if my leftmin is 0   
        # if my leftmax every becomes negative though ima return false because that means theres an early close parentheses 

        leftmin, leftmax = 0, 0 

        for i in s: 
            if i == "(":
                leftmin, leftmax = leftmin + 1, leftmax + 1 
            elif i == ")": 
                leftmin, leftmax = leftmin - 1, leftmax - 1 
            else: 
                # all my posssibilities 
                leftmin, leftmax = leftmin - 1, leftmax + 1 
                
            if leftmax < 0:  
                return False  

            if leftmin < 0:  
                leftmin = 0  

        return leftmin == 0 

                
        
