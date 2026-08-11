class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return []
        answer=[]
        def res(par, x, remain):
            if remain == 0:
                answer.append(par)
            elif x>=remain:
                par+=')'
                res(par,x-1,remain-1)
            elif x==0:
                par+='('
                res(par,x+1,remain-1)
            else:
                par1 = par+'('
                par+=')'
                res(par1,x+1,remain-1)
                res(par,x-1,remain-1)
        res("",0,n*2)
        return answer