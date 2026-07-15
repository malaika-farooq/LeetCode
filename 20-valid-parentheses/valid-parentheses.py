class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                lst.append(s[i])
            else:
                if len(lst) > 0:
                    last = lst.pop()
                    if s[i] == ')':
                        if last != '(': return False
                    elif s[i] == ']':
                        if last != '[': return False
                    elif s[i] == '}':
                        if last != '{':  return False
                else:
                    return False

            
        if len(lst) > 0:
             return False
        return True


