class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answer = []

        def backtrack(start: int, remain: int, path: list[int]) -> None:
            if remain == 0:
                answer.append(path.copy())
                return

            for i in range(start, len(nums)):
                n = nums[i]
                if n > remain:
                    break

                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(n)
                backtrack(i, remain - n, path)  # allow reusing same number
                path.pop()

        backtrack(0, target, [])
        return answer