class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp={}
        for i in reversed(range(len(nums))):
            maximum=0
            for k in range(i,len(nums)):
                if nums[k]>nums[i] and dp[k]>maximum:
                    maximum=dp[k]
            dp[i]=1+maximum
        
        return max(dp.values())
        
        