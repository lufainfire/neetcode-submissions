class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        max = 1
        flag = 0
        output = []
        #find max
        for i in nums:
            if i!=0:
                max = max * i
            else:
                flag= flag+1
        #divide by x 
        for x in nums:
            if x==0 and flag<2:
                output.append(int(max))
            elif flag==0:
                output.append(int(max/x))
            else:
                output.append(0)

        return output
            
            

