from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        for i in s:
            print(i)
            if i == '(':
                q.append(')')
            elif i == '[':
                q.append(']')
            elif i == '{':
                q.append('}')
            else:
                if len(q)>0 and q.pop() == i:
                    continue
                else:
                    return False
        if len(q) == 0:
            return True
        else:
            return False
        