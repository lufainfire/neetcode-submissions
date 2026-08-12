class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot = len(gas)
        curr = gas[0]-cost[0]
        start=0
        end=0
        while start!=(end+1)%tot:
            if curr<0:
                if start==0:
                    start=tot-1
                else:
                    start-=1
                curr += gas[start] - cost[start]
            else:
                end+=1
                curr+= gas[end]-cost[end]
                

        if curr<0:
            return -1
        else:
            return start



        
        