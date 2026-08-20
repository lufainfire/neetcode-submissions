class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1={}
        dp2={}
        def helper(nums: List[int], dp): 
            value = dp.get(len(nums),-1)
            if value != -1:
                return value

            if len(nums)==0:
                return 0
            elif len(nums)==1:
                return nums[0]
            elif len(nums)==2:
                return max(nums[0],nums[1])
            result = max((nums[0]+helper(nums[2:], dp)), (helper(nums[1:], dp)))
            dp[len(nums)] = result

            return result
        return max(helper(nums[:-1], dp1), helper(nums[1:], dp2))