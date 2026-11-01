class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer=0
        # store the min so far
        val=prices[0]
        for i in prices:
            val = min(i,val)

            answer= max(answer,i-val)
        return answer
        