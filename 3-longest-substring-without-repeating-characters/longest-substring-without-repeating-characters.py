class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        prev = 0
        current = 0
        maxcount = 0
        for current in range(len(s)):
            while s[current] in sub:
                sub.remove(s[prev])
                prev +=1
            sub.add(s[current])
            maxcount = max(maxcount, current - prev + 1)
        return maxcount
 
