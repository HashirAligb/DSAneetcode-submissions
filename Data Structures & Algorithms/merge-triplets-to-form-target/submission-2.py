class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # ill have a set where ill add the indices if a triplet is a match with the target 
        # i knwo that a array in our triplet set is useless if any of the vals in it is 
        # greater than any in my target array so i can just continue past that subarray 
        # for the remaining subarrays that ARE valid what i'll do is compare if any vals in it 
        # are == to my targets and then add to my set accordingly then ill return if the len of my set is equal to target 


        ans = set()  

        # ** FOR CLARITY ** 
        # t is my subarray, and my i is the index of that subarr and n is the val

        for t in triplets: 
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]: 
                continue 
            for i, n in enumerate(t):  
                if n == target[i]: 
                    ans.add(i) #using the set and adding the index only cuz a set is for UNIQUE values no two indices could ever be the same

        return len(ans) == len(target) 

