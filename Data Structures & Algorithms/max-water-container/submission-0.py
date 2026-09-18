class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum=0
        left=0
        right=len(heights)-1
        while left<right:
            maximum=max(maximum,
            min(heights[left],heights[right])*(right-left))

            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        return maximum
        