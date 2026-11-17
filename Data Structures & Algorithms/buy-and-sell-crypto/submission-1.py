class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer=0
        val = prices[0]
        for n in prices:
            val = min(val,n)
            answer = max(answer, n-val)
        return answer

        