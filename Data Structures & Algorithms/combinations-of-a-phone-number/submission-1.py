class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # a-b-c -> 2    range is (n-2)*3 and (n-1)*3
        answers=[]
        def rec(start, curr):
            if not start:
                if curr != "":
                    answers.append(curr)
            else:
                n = (int(start[0])-2)*3
                if int(start[0])==7:
                    for i in range(n, n+4):
                        rec(start[1:],curr+chr(ord('a')+i))
                elif int(start[0])==8:
                    n+=1
                    for i in range(n, n+3):
                        rec(start[1:],curr+chr(ord('a')+i))
                elif int(start[0])==9:
                    for i in range(n+1, n+5):
                        rec(start[1:],curr+chr(ord('a')+i))
                else:
                    for i in range(n, n+3):
                        rec(start[1:],curr+chr(ord('a')+i))
        rec(digits,"")
        return answers
        