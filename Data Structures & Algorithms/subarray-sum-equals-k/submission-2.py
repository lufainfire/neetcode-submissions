class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 
        dp={0:[1]}
        answer=0
        tot=0
        for i, n in enumerate(nums): # tot - target = k
            tot+=n
            if tot-k in dp:
                for x in dp[tot-k]:
                    answer+=1
            if tot in dp:
                dp[tot].append(i)
            else:
                dp[tot]=[i]
        print(dp)

            
        return answer




        



        