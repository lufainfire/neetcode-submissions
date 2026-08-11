class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        answers =[]
        i=0
        for num in nums:
            hashMap[target-num]=i
            i+=1
        i=0
        for num in nums:
            answer = hashMap.get(num)
            if answer != None and i!=answer:
                return [i,answer]
            i+=1
        return []