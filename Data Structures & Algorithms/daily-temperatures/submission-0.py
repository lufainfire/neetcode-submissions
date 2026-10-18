class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i= len(temperatures)-2
        mp={len(temperatures)-1:0}
        def search (ptr, start): #ptr: 
            if temperatures[ptr] > temperatures[start]:
                return ptr-start
            elif mp[ptr] ==0:
                return 0
            else:
                return search(ptr+mp[ptr], start) 

        while i >=0:
            x = search(i+1, i)
            mp[i] = x
            i-=1
        answer=[]
        for x in range(len(temperatures)):
            answer.append(mp[x])
        return answer


        