class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #end start
        #O(1) O(n)
        start=0
        end=0
        #aabbb -> bbaaa x
        #
        answer=False
        w = set()
        s = {}
        for i in s1:
            w.add(i)
            if i in s:
                s[i]+=1
            else:
                s[i]=1
        curr={}
        # ab
        print(len(s2))
        print(w)
        print(s)
        while end < len(s2):
    
            i=s2[end]
            if i not in w:
                end+=1
                start=end
                curr={}
            else:
                end+=1
                #add letter
                if i in curr:
                    curr[i]+=1
                else:
                    curr[i]=1
                #if curr[i] > s[i] then we need to backtrack and remove old i
                if curr[i] > s[i]:
                    for z in range(start, end):
                        #remove z
                        curr[s2[z]]-=1
                        start+=1

                        #check if remove old i
                        if curr[i] <= s[i]:
                            break
            if curr == s:
                answer=True
                break    
        return answer
                

                




            
            




       
        



        