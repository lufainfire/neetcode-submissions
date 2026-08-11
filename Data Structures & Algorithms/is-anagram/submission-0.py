class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #make hashmap with letter and frequency of s 
        map={}
        for c in s:
            map[c]= map.get(c,0)+1
        #check if anagram holds
        for c in t:
            if c in map: #good
                map[c]-=1
            else:   #bad
                return False

        for num in map.values():
            if num!=0:
                return False
        
        return True