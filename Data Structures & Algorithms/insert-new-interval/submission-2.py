class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # just do a Binary Search, find where the element fits
        #check if 
        #where do we start -> is it overlapping 
        #do i start in ennemy territory
        #do i finish in ennemy territory
        #do i traverse ennemy territory
        if len(intervals) == 0:
            return [newInterval]
        traverse=set() #store the index of traversed interva

        start=newInterval[0]
        end=newInterval[1]
        
        for i,n in enumerate(intervals): 
            if start <= n[1] and n[0] <= end:
                start=min(start, n[0])
                end=max(end,n[1])
                traverse.add(i)
        newInter = [val for i, val in enumerate(intervals) if i not in traverse]
        flag=True
        for i in range(len(newInter)):
            if newInter[i][0] > start:
                newInter.insert(i,[start,end])
                flag=False
                break
        if flag:
            newInter.append([start,end])
        return newInter
        

            
            


            


        
            
