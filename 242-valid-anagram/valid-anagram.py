class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for anagram, shortcut is sortign, sort both and the reuslt will be same for both, if not then not anagram

        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
