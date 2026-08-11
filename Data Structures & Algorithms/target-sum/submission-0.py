class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        total=0
        for item in nums:
            total+=item
        def helper(nums,count):
            if len(nums)==0:
                if count == target:
                    return 1
                else:
                    return 0
            value = dp.get( (count, len(nums)), -1)
            if value !=-1:
                return value
            
            result = helper(nums[1:],count+nums[0]) + helper(nums[1:],count-nums[0])
            dp[(count,len(nums))]=result
            return result
        return helper(nums,0)

            



        