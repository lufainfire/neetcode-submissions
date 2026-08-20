class Solution:
    def findMin(self, nums: List[int]) -> int:
        def rec(left, right):
            if left >= right:
                return nums[right]
            mid = (left+right)//2
            if nums[mid]>nums[right]:
                return rec(mid+1, right)
            else:
                return rec(left, mid)
        return rec(0, len(nums)-1)
        