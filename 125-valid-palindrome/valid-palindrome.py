class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        s = s.lower()
        string = "".join(c for c in s if c.isalnum())
        right = len(string) -1

        while left < right:
            if string[left] == string[right]:
                left +=1
                right -=1
            else:
                return False
            
        return True

        
