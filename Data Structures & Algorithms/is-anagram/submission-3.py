class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}
        for i in s:
            freq_s[i] = freq_s.get(i,0)+1
        for i in t:
            freq_t[i] = freq_t.get(i,0)+1
        
        return True if freq_s == freq_t else False
        