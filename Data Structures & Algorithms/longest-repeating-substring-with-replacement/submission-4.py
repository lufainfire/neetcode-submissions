class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window
        #edge case when we finish
        #when do we restart at first change
        #start and end index
        #what if k == 0

        answer=1
        start=0
        end=0
        restart=-1
        curr=s[0]
        count=0
        while start < len(s)-1:
            if end >= len(s):
                if answer > end-start + k:
                    break
                answer = max(answer, end-start+ min(start, k-count))
                curr=s[start+1]
                start=start+1
                end=start+1
                count=0
            elif s[end] == curr:
                answer=max(answer,end-start+1)
                end+=1
            else:
                if count == 0:
                    restart = end
                    
                if count < k:
                    answer=max(answer,end-start+1)
                    end+=1
                    count+=1
                else:
                    #restart at restart
                    curr=s[restart]
                    start=restart
                    end=restart
                    count=0
        answer = max(answer, end-start+ min(start, k-count))
        return answer 
        
                    


                
            





        