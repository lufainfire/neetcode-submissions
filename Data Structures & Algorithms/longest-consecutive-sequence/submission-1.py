class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            if num in map:
                continue
            left_pos = num-1
            right_pos = num+1
            left = 0
            right=0
            if left_pos in map:
                left=map[left_pos]
            if right_pos in map:
                right=map[right_pos]
            total = 1 + left + right
            while left_pos in map:
                map[left_pos]=total
                left_pos-=1
            while right_pos in map:
                map[right_pos]=total
                right_pos+=1
            map[num]=total
        result = 0
        for val in map.values():
            if val>result:
                result=val
        return result

            