class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True
        s = s.lower()
        string=""
        for c in s:
            if (ord(c)- ord('a') >= 0 and ord(c)-ord('z')<=0) or (ord(c)-ord('0') >= 0 and ord(c)-ord('9') <= 0):
                string+=c
        left = len(string)//2-1
        right = len(string)//2

        if len(string)%2 != 0:
            right+=1
        while left > -1 and right < len(string):
            if string[left] != string[right]:
                return False 
            left-=1
            right+=1
        return True

        

        