class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        #first we want to have two ptrs to go through word an abbr 
        # next we want to check if the letters in each ae equal 
        # an abbr cant have a 0 to start with so we check for that as a case
        # also we wanna check if the word and abbr end at the same time so thats what we return 
        # also we wanna create a var called sublen and the reason we multply by ten  
        # is to be able to colected the digits in a proper fashion 

        i, k = 0, 0 

        while i < len(word) and k < len(abbr): 
            if word[i] == abbr[k]: 
                i, k = i + 1, k + 1
            elif abbr[k].isalpha() or abbr[k] == "0": 
                return False 
            else: 
                sublen = 0 
                while k < len(abbr) and not abbr[k].isalpha(): 
                    sublen = sublen * 10 + int(abbr[k]) 
                    k = k + 1 
                i = i + sublen 
        return i == len(word) and k == len(abbr)