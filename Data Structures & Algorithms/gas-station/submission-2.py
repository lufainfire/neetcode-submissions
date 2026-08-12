class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current=0
        answer=0
        if sum(gas)-sum(cost)<0:
            return -1
        for n in range(len(gas)):
            current+=gas[n]-cost[n]
            if current<0:
                answer=n+1
                current=0
        return answer                






        
        