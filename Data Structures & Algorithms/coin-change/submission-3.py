from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque()
        q.append((0,0))
        dp=set()
        # sum 
        while q:
            data = q.pop()
            sum = data[0]
            rank = data[1]
            if sum == amount:
                return rank
            elif sum > amount or sum in dp:
                continue
            dp.add(sum)
            for coin in coins:
                if coin+sum<= amount:
                    q.appendleft((coin+sum,rank+1))
        return -1

        

