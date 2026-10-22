class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #code
        #tcode or t is inside
        #carneetcode carneet is carneetcode is car is
        word=[0]
        for i in range(len(s)):
            for start in word:
                if s[start:i+1] in wordDict:
                    word.append(i+1)
                    break
        if len(s) in word:
            return True
        else:
            return False
        

        