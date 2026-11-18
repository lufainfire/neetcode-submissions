class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit=set()
        left=0
        right=0
        answer=0
        while right < len(s):
                #backtrack left until s[right]=s[left]
            while s[right] in visit:
                visit.remove(s[left])
                left+=1
            answer=max(answer, right-left+1)
            visit.add(s[right])
            right+=1
        return answer
        

            
            