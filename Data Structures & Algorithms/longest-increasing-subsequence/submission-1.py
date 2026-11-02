class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP problem O(n^2) memo -> dp[i+1] = 
        # bind to biggest sub
        # dict -> memo[i] = len(subsq)
        # for loop
        right = len(nums)-1
        memo={}
        answer=1
        # make memo = {i: 1} for i in range(len(nums))
        while right >= 0:
            val=0
            for i in range(right,len(nums)):
                if nums[right]<nums[i]:
                    val = max(val, memo[i])
            memo[right]=val+1
            answer=max(answer,val+1)
            right-=1

        return answer

                


        