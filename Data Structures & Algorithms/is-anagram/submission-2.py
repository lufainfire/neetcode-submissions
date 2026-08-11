class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #make hashmap with letter and frequency of s 
        map={}
        for c in s:
            map[c]= map.get(c,0)+1

        #check if anagram holds
        for c in t:
            if c in map and map[c]>0: #good
                map[c]-=1
            else:   #bad
                return False
        return True