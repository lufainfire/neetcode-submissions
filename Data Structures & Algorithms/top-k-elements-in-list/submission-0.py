class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        answer=[]
        for n in nums:
            if n in f:
                f[n] = f[n]+1
            else:
                f[n] = 1
        g = dict(sorted(f.items(), key=lambda x: x[1], reverse=True))
        count=1
        for e in g:
            if count<=k:
                answer.append(e)
            else:
                break
            count+=1            
        return answer
        