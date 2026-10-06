class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # num : size, left index, right index
        dp={}
        answer=0
        for n in nums:
            if n in dp:
                continue
            if n-1 in dp and n+1 in dp:
                
                left = dp[n-1][1]
                right = dp[n+1][2]
                size = right-left+1
                #modify left
                dp[left]=(size,left,right)
                dp[right]=(size,left,right)
                answer=max(answer,size)
            elif n-1 in dp:
                
                left = dp[n-1][1]
                size = n-left+1
                #modify
                dp[left]= (size,left,n)
                dp[n] = (size,left,n)
                answer=max(size,answer)
            elif n+1 in dp:
                right= dp[n+1][2]
                size = right-n+1
                dp[n] = (size,n,right)
                dp[right] = (size,n,right)
                answer=max(size,answer)
            else:
                dp[n] = (1,n,n)
                answer=max(1,answer)

        
        return answer
            

        