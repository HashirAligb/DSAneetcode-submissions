class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
   
        people.sort() 

        boats = 0 
        left, right = 0, len(people) - 1 

        while left <= right: 
            diff = limit - people[right] #so we can check if we can make a pair 
            right -= 1 #either way we decrement in every case 
            boats += 1 
            if left <= right and diff >= people[left]: 
                left += 1 
                 
        return boats 
            
                