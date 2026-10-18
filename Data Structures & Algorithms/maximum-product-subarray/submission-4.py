class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #two choice:
        #choose to include nums[i] or choose dp[i-1]
        #second option is really simple cuz we already have the answer stored in dp
        # first option in the other hand is kinda tricky becuase
        # if nums[i] is negative vs positive
        #what if dp[i-1] contains 3 value:
        # max anwer, max answer containing i-1, max negative answer
        dp = [(nums[0],nums[0],nums[0])]
        answer=nums[0]
        for i in range(1,len(nums)):
            n=nums[i]
            
            sol2=max(n, n*dp[i-1][1],n*dp[i-1][2])
            sol3=min(n, n*dp[i-1][1],n*dp[i-1][2])
            sol1=max(dp[i-1][0],sol2)
            answer=max(sol1,answer)
            dp.append((sol1,sol2,sol3))
        return answer
            

        
