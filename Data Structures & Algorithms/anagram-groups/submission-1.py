class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def isAnagram(first, second):
            anagram = {}
            for n in first:
                if n in anagram:
                    anagram[n]+=1
                else:
                    anagram[n]=1

            for n in second:
                if n in anagram:
                    anagram[n]-=1
                else:
                    return False
            
            for n in anagram:
                if anagram[n]!=0:
                    return False
            return True
        answer=[]
        while strs != []:
            first = strs.pop()
            sublist=[first]
            delete=[]
            for i, num in enumerate(strs):
                if isAnagram(first, num):
                    sublist.append(num)
                    delete.append(i)
            answer.append(sublist)
            for x in delete[::-1]:
                del strs[x]
        return answer
