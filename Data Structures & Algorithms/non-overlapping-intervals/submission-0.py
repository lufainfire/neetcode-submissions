class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        size=len(intervals)
        nums=[]
        for i,n in enumerate(intervals):
            nums.append((n[0],0,i))
            nums.append((n[1],1,i))
        def mysort(n):
            if n[1] == 0:
                return n[0]+0.1
            else:
                return n[0]
        nums.sort(key=mysort)
        alive=set()
        killed=set()
        for n in nums:
            val = n[0]
            typ = n[1]
            i = n[2]
            if i in killed:
                continue
            if typ == 0:
                alive.add(i)
            else:
                alive.discard(i)
                if alive:
                    killed = killed | alive
                alive=set()
        return len(killed)
        
        