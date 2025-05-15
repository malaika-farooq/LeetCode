class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        prev = 0
        freq = 0
        for current in range(len(s)):
            while s[current] in window:
                window.remove(s[prev])
                prev += 1
            window.add(s[current])
            freq = max(freq, current - prev + 1)
        return freq
