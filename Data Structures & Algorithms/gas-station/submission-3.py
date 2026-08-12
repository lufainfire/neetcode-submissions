class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas)<sum(cost):
            return -1
        
        current=0
        answer=0

        for n in range(len(gas)):
            current+=gas[n]-cost[n]
            if current<0:
                answer=n+1
                current=0
        return answer                






        
        