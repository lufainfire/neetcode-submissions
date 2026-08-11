class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = {}
        result = 0
        for num in nums:
            if num in map:
                continue
            left = map.get(num-1,0)
            right = map.get(num+1,0)
            total = 1 + left + right
            result = max(result, total)
            map[num-left]=total
            map[num+right]=total
            map[num]=total
        return result

            