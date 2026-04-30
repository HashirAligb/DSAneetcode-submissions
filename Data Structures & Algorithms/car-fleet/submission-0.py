class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #im going to sort the position and speeds as tuples in an arr 
        #next im gonna use a stack to se wherever the cars collides to become fleets 
        # ill be going through it in reverse order and pop whenevr thres a collision 
        # i find out if theres a collision when my current cars time reached the tagret before the previous 
        # lastly i can just return the lenght of my stack because thats how many fleets i have 

        fleets = [(p,s) for p, s in zip(position, speed)] 
        stack =  [] 

        for p, s in sorted(fleets)[::-1]:  
            stack.append((target - p) / s)  

            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop() 
        return len(stack) 
