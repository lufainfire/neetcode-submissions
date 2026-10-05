class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dp={}
        answer=0
        start=-1
        for i, n in enumerate(s):

            if n in dp and dp[n]>=start:
                start = dp[n]  
            else:
                answer=max(answer,i-start)
            dp[n]=i
        return answer
                