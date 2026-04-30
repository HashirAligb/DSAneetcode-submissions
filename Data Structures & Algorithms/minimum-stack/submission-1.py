class MinStack:

    def __init__(self):
        self.stack = []    
        self.minStack = []               #create two stacks 
                                #one will be the stack and then ill have one for thr minvalue 
    def push(self, val: int) -> None:
        self.stack.append(val) 
        val = min(val, self.minStack[-1] if self.minStack else val) 
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1] 

    def getMin(self) -> int:
        return self.minStack[-1]
