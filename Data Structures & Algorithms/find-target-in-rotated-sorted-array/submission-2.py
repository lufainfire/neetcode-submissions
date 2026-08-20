class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bst(start, end):

            if start == end and nums[start] == target:
                return start
            if start >= end:
                return -1
            if nums[start]>target or target>nums[end]:
                return -1
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                return bst(start, mid-1)
            else:
                return bst(mid+1, end) 
        
            
            
        def rec(start, end):
            if start == end and nums[start] == target:
                return start
            if start >= end:
                return -1
            
            if nums[start]<nums[end]:
                return bst(start, end)

            mid = (start+end)//2
            return max(rec(start, mid), rec(mid+1, end))
        return rec(0, len(nums)-1)

        