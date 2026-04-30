class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # ill get my index and val in a map to mark down all the indexes of my alien dict  
        ordermap = {n : i for i, n in enumerate(order)} 

        for i in range(len(words) - 1): 
            w1, w2 = words[i], words[i+1] 

            for j in range(len(w1)): 
                if j == len(w2): 
                    return False 
                if w1[j] != w2[j]: 
                    if ordermap[w1[j]] > ordermap[w2[j]]: 
                        return False 
                    break  
        return True 
