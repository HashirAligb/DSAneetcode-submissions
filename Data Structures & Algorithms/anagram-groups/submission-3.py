class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        hashset = defaultdict(list) 


        for words in strs:  
            count = [0] * 26 
            for i in words:  
                count[ord("a") - ord(i)] += 1 

            hashset[tuple(count)].append(words) 



        res = []
        for i, n in hashset.items(): 
            res.append(n)
        return res             