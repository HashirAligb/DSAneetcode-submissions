class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # i need a hashmap to count the longest sequence
        # I need to store the count of the seuqneces
        # I am going to store them in an array and compare 
        # max()


        seen = set(nums)
        longest = 0

        for i in seen:
            if i - 1 not in seen:
                start = 1
                while i + start in seen:
                    start += 1
                longest = max(longest, start)
        

        return longest
        


            

        

    



                


        
