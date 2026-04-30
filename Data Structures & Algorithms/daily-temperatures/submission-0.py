class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        temp = temperatures 
        n = len(temp) 
        res = [0] * n   
        stack = []
        for i, k in enumerate(temp):
            while stack and stack[-1][0] < k:
                stackT, stackI = stack.pop() 
                res[stackI] = i - stackI  
            stack.append([k,i])
        return res 


