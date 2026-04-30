class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        


        hashmap = defaultdict(list) 


        for i in strs:
            ord_chart = [0] * 26 


            for w in i:
                ord_chart[ord(w) - ord('a')] += 1   

            hashmap[tuple(ord_chart)].append(i) 
        

        res = [] 

        for i in hashmap.values(): 
            res.append(i) 
        return res 
