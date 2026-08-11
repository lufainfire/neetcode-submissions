class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        answer = []
        def dfs(i, prev: list[int]):
            if i == len(nums):
                answer.append(prev.copy())
                return
            elif i> len(nums):
                return
            #right
            dfs(i+1, prev.copy())
            #left
            prev.append(nums[i])
            dfs(i+1, prev.copy())
        dfs(0,[])
        return answer