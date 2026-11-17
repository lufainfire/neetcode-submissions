class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1,2,3    5,6,7 -> 4    value[3] + value[5] + 1 then it will change value[4 - value[3] ] to
        # change value[4 + value[5]]
        # answer = max(answer, value[3] + value[5] + 1)
        # left and right in value
        # only left in vlaue
        # only right in value
        # none -> value[curr] = 1

        value={}
        visit=set()
        answer=0
        
        for n in nums:
            if n in visit:
                continue
            elif n-1 in value and n+1 in value:
                v = value[n-1] + 1 + value[n+1]
                value[n - value[n-1]] = v
                value[n + value[n+1]] = v

            elif n-1 in value: #only left
                v = value[n-1] + 1
                value[n - value[n-1]]=v
                value[n] = v                
            
            elif n+1 in value:
                v = value[n+1] + 1
                value[n + value[n+1]]=v
                value[n] = v 

            else:
                value[n] = 1
                v=1
            
            visit.add(n)
            answer=max(answer,v)
        return answer
        