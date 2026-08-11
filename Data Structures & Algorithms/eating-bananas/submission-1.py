class Solution:
    big=0
    result=0
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        big=0
        for n in piles:
            big=max(big,n)
        def isValid(k):
            total=0
            for n in piles:
                if n%k==0:
                    total+=n/k
                else:
                    total+=(n+(k-n%k))/k
            return(total<=h)
        def bst(low,high):
            if low>high:
                return big
            mid=int((high-low)/2+low)
            if isValid(mid):
                return(min(bst(low,mid-1),mid))
            else:
                return bst(mid+1,high)
        return bst(1,big)

        