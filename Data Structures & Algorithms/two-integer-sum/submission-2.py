class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        look = {}
        for i,n in enumerate(nums):
            if target-n in look:
                return [look[target-n],i]
            if n not in look:
                look[n] = i
        