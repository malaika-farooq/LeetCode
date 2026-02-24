class Solution:
    def romanToInt(self, s: str) -> int:
        resp = 0
        hashset = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}  
        for i, st in enumerate(s):
            if st in hashset:
                if i < len(s)-1 and hashset[s[i]] < hashset[s[i+1]]:
                    resp -= hashset[st]
                else:
                    resp += hashset[st]

        return resp

        


