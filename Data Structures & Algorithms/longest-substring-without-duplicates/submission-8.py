class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        start=0
        end=0
        answer=0
        # if s[end] in visit -> backtrack start until remove the "bad" item
        while end<len(s):
            if s[end] in visit:
                while s[start] != s[end] and start < end: #maybe start <= end
                    visit.remove(s[start])
                    start+=1
                start+=1
            else:
                visit.add(s[end])
            end+=1
            answer=max(answer, end-start)
        return answer