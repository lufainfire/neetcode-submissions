class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start =0
        end=0
        def bs(start, end, t):
            if start > end:
                return -1

            mid = (start+end)//2
            if numbers[mid] == t:
                return mid
            elif numbers[mid] < t:
                return bs(mid+1, end, t)
            else:
                return bs(start, mid-1,t)
        
        left=0
        answer=[]
        for i in range(len(numbers)):
            t = target - numbers[i]
            sol=bs(i+1,len(numbers)-1,t)
            
            if sol != -1:
                answer= [i+1,sol+1]
                break
        return answer
            
        