class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        hm = {}
        visit=set()
        visit1=set()
        for i, num in enumerate(nums):
            if -num in hm:
                hm[-num].append(i)
            else:
                hm[-num]=[i]
        print(hm)
        for i, n in enumerate(nums):
            if n in visit1:
                continue
            else:
                visit1.add(n)
            for k in range(i,len(nums)):
                m = nums[k]
                if i!=k and m+n in hm:
                    for num in hm[m+n]:
                        if num>k:
                            if {n,m,nums[num]} not in visit:
                                answer.append((n,m,nums[num]))
                                visit.add(frozenset({n,m,nums[num]}))
                            break
                          

                    
            

        
        return answer