class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer=[]
        nums.sort()

        def adding(sum: int, prevnums: list [int], i: int):
            if sum == target:
                answer.append(prevnums.copy())
                return 
            elif sum > target or i >= len(nums):
                return None
            else:
                adding(sum,prevnums.copy(), i+1)
                left = prevnums.copy()
                left.append(nums[i])
                adding(sum+nums[i], left, i)
                   
        adding(0, [], 0)
        return answer