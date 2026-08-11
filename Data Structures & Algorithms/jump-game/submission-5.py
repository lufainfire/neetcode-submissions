class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach=0
        tot = len(nums)-1
        if tot == 0:
            return True
        for i, v in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + v)
            if reach >= tot:
                return True
        return True

                
            
        

        