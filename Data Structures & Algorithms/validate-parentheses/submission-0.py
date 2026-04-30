class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoOpen = { ")" : "(", "]":"[", "}":"{" }

        for c in s: 
            if c in closetoOpen: 
                if stack and stack[-1] == closetoOpen[c]:  #checks if it isnt empty and the top of the stack is the mapped to the correct open thing
                    stack.pop() # removes it 
                else: 
                    return False
            else: 
                stack.append(c)
        if not stack: 
            return True
        else: 
            return False 
