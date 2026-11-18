from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        for c in s:
            if c == '[':
                q.append(']')
            elif c == '(':
                q.append(')')
            elif c == '{':
                q.append('}')
            else:
                if len(q) == 0:
                    return False
                r = q.pop()
                if r != c:
                    return False
        if len(q) != 0:
            return False
        else:
            return True
            
        
        