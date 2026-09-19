class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        answer=0
        h=len(grid)
        w=len(grid[0])
        def visit(x,y):
            if (x,y) in visited or x<0 or y<0 or y>=h or x>=w or grid[y][x]==0:
                return 0
            visited.add((x,y))
            return 1+visit(x-1,y)+visit(x+1,y)+visit(x,y-1)+visit(x,y+1)

        for i in range(h):
            for j in range(w):
                answer=max(answer, visit(j,i))
        return answer
            
            
        