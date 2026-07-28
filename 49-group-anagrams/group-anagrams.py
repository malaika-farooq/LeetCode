class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        self.result = {}
        
        # no need for brute force, just use dictionary to take key as main sorted words as they are unique and then put in the words in it and return the values of the dictionary in the end, for default it returns the keys so use values() function to return it
        for s in strs:
            key = tuple(sorted(s))
            if key not in self.result:
                self.result[key] = []
            self.result[key].append(s)
        
        
        return list(self.result.values())




        