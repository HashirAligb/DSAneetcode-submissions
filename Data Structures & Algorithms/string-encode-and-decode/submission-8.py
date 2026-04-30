class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res
        
    def decode(self, s: str) -> List[str]:

        res, count = [], 0
        while count < len(s):
            j = count
            while s[j] != "#":
                j += 1
            length = int(s[count:j])
            res.append(s[j + 1 : j + 1 + length])
            count = j + 1 + length
        return res
        
        



        