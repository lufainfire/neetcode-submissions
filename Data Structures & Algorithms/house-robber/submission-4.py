class Solution:
    def rob(self, nums: List[int]) -> int:
        dp={}
        def helper(nums: List[int]): 
            value = dp.get(len(nums),-1)
            if value != -1:
                return value

            if len(nums)==0:
                return 0
            elif len(nums)==1:
                return nums[0]
            elif len(nums)==2:
                return max(nums[0],nums[1])
            result = max((nums[0]+helper(nums[2:])), (helper(nums[1:])))
            dp[len(nums)] = result

            return result
        return helper(nums)