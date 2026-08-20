class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        def isPal(left, right):
            count=""
            if left == right:
                count+=s[left]
                left-=1
                right+=1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    count=s[left]+count+s[right]
                else:
                    break
                left-=1
                right+=1
            return count
        answer=""
        for i in range(len(s)-1):
            res = isPal(i,i)
            if len(res)>len(answer):
                answer=res
            res=isPal(i,i+1)
            if len(res)>len(answer):
                answer=res
        res = s[-1]
        if len(res)>len(answer):
            answer=res 
        return answer
            
            
