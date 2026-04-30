class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        freqS = Counter(s) 
        freqT = Counter(t) 

        for i in s: 
            if i not in freqT or freqS[i] != freqT[i]: 
                return False 
        return True 


        