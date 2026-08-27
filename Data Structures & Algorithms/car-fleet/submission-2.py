class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(speed)==1:
            return 1
        nums = list(zip(position, speed))
        
        answer=1
        nums.sort()
        left = len(nums)-2
        right = len(nums)-1
        while left>=0:
            
            if ( (target-nums[left][0])/nums[left][1]) <= ((target-nums[right][0])/nums[right][1]):
                left-=1

            else:
                right=left
                answer+=1
                
                left-=1
        return answer
        