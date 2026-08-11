class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        def rec(nums, res):
            if not nums:
                answer.append(res)
            
            for i, num in enumerate(nums):
                new_num = nums.copy()
                del new_num[i]
                new_res = res.copy()
                new_res.append(num)
                rec(new_num, new_res)
        rec(nums,[])
        return answer


        