class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def rec(start,n):
            if n-start <= 1:
                return
            #n=3
            #start=1
            #i=1
            # [6,7]
            # [10,11]

            for i in range(start,n-1):
                a=matrix[start][i]
                b=matrix[i][n-1]
                d=matrix[n-1-i+start][start]
                c=matrix[n-1][n-1-i+start]
                matrix[start][i]=d
                matrix[i][n-1]=a
                matrix[n-1-i+start][start]=c
                matrix[n-1][n-1-i+start]=b
            rec(start+1,n-1)
        rec(0,len(matrix))
        
        


        