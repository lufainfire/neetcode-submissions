class Solution:
    def trap(self, height: List[int]) -> int:
        might = 0
        high=0
        answer=0
        left=0
        lval=0
        rval=0
        right=len(height)-1
        while left <= right:
            if rval > lval: #move left
                if height[left]< lval:
                    answer+=lval-height[left]
                else:
                    lval=height[left]
                left+=1

            else:
                if height[right] < rval:
                    answer+= rval-height[right]
                else:
                    rval = height[right]
                right-=1


        return answer