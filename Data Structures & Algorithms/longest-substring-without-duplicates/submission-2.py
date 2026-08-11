class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        map={}
        count=0
        limit=0
        for c in s:
            count+=1
            if map.get(c,-1)>limit:
                limit = map[c]

            else: #good
                result=max(result,count-limit)
            map[c]=count
        return result


            

        