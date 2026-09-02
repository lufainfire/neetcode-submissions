import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1:
            return 1
        
        return int(math.comb(n+m-2,n-1))
        