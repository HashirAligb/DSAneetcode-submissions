class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #this is the floyd algo 
        #im using a slow and fast to find the intersection point 
        # then i use a new slow ptr to see where that actual duplicate is because the  
        # intersction of the beginning slow ptr and the first one is the duplicate value 

        fast, slow = 0, 0 

        while True: 
            slow = nums[slow] 
            fast = nums[nums[fast]] 

            if slow == fast: 
                break 
        slow2 = 0 

        while True:
            slow = nums[slow] 
            slow2 = nums[slow2] 

            if slow == slow2: 
                return slow
        