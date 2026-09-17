class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #check for rows
        s=set()
        for rows in board:
            s.clear()
            for n in rows:
                if n == ".":
                    continue
                x=int(n)
                if x in s:
                    return False
                else:
                    s.add(x)
        #check for columns
        for j in range(0,9):
            s.clear()
            for i in range(0,9):
                n=board[i][j] #might want to change order
                if n == ".":
                    continue
                x=int(n)
                if x in s:
                    return False
                else:
                    s.add(x)
        #check for square:
        for y in range(0,3):
            for w in range(0,3):
                s.clear()
                for i in range(0,3):
                    for j in range(0,3): #2+ 3*2=8
                                            
                        n=board[i+3*y][j+3*w] #might want to change order
                        if n == ".":
                            continue
                        x=int(n)
                        if x in s:
                            return False
                        else:
                            s.add(x)
        return True




        

                
        

        