class Solution:
    def countSubstrings(self, s: str) -> int:
        count=len(s)
        for i in range(1,len(s)-1):
            m=1
            while i+m < len(s) and i-m >= 0:
                if s[i+m]==s[i-m]:
                    count=count+1
                    m=m+1
                else:
                    break
        for i in range(len(s)-1):
            m=1
            while i+m < len(s) and (i-m+1) >= 0:
                if s[i+m]==s[i-m+1]:
                    count=count+1
                    m=m+1
                else:
                    break            
        return count


            
            
        