class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #two choice:
        #choose to include nums[i] or choose dp[i-1]
        #second option is really simple cuz we already have the answer stored in dp
        # first option in the other hand is kinda tricky becuase
        # if nums[i] is negative vs positive
        #what if dp[i-1] contains 3 value:
        # max anwer, max answer containing i-1, max negative answer
        currMin = nums[0]
        currMax = nums[0]
        answer=nums[0]
        for i in range(1,len(nums)):
            
            n=nums[i]
            if n == 0:
                currMin=0
                currMax=0
                answer=max(answer,0)
            else:
                sol2=max(n, n*currMax,n*currMin)
                sol3=min(n, n*currMax,n*currMin)
                answer=max(sol2,answer)
                currMax=sol2
                currMin=sol3
        return answer
            

        
