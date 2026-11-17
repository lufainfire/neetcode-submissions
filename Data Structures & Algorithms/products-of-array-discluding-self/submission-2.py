class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = [[0 for _ in range(2)] for _ in range(len(nums))]
        c[0][0]=nums[0]
        c[-1][1]=nums[-1]
        end=len(nums)-2
        start=1
        while start < len(nums):
            c[start][0]=c[start-1][0]*nums[start]
            start+=1
        while end >= 0:
            c[end][1] = c[end+1][1]*nums[end]
            end-=1
        
        answer=[0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                answer[i] = c[i+1][1]
            elif i == len(nums)-1:
                answer[i] = c[i-1][0]
            else:
                answer[i] = c[i-1][0]*c[i+1][1]
        
        return answer

        