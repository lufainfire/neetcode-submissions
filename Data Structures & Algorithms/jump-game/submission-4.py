class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        current=0
        while current < len(nums) :
            if nums[current] == 0:
                return False
            
            max_val=-1
            for n in range(1,nums[current]+1):
                pos = current+n
                if pos>=len(nums)-1:
                    return True
                
                if max_val <= (nums[pos]+n) and nums[pos]!=0:
                    max_val = nums[pos]+n
                    max_pos = pos
            if max_val == -1:
                return False
            current=max_pos
        return True

                
            
        

        