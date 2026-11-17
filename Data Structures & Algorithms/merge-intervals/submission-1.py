class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort using smallest first element
        # O(n^2) can i do better O(nlogn) because you don't have to compare to every single other interval as soon as you cant u stop 2n
        #if while overlapp
        def myVal(num):
            return num[0]

        intervals.sort(key=myVal)
        s=0
        answer=[]
        while s<len(intervals)-1:
            if intervals[s][1] >= intervals[s+1][0]:
                intervals[s+1][0]=min(intervals[s][0],intervals[s+1][0])
                intervals[s+1][1]=max(intervals[s][1],intervals[s+1][1])
                
            else:
                answer.append(intervals[s])   
            s+=1
        answer.append(intervals[s])
        return answer
                



        
        