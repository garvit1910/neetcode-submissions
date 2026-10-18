from collections import deque 
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visit=set ()
        queue=deque()
        ROWS, COLUMNS= len(grid), len(grid[0])
        if grid[0][0]==1 or grid[ROWS-1][COLUMNS-1]:
            return -1
        queue.append((0,0))
        visit.add((0,0))
        length= 1
        while queue:
            for i in range(len(queue)): 
                r, c =queue.popleft()
                if r==ROWS-1 and c==COLUMNS-1 and grid[r][c]==0:
                    return length
                directions=[[1,0], [-1,0], [0,1],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]
                for dr, dc in directions: 
                    nr, nc= r+dr, c+dc
                    if min(nr, nc) < 0 or nr==ROWS or nc==COLUMNS or grid[nr][nc]==1 or (nr,nc) in visit: 
                        continue 
                    queue.append((nr,nc))
                    visit.add((nr,nc))
            length+=1
        if len(queue)==0: 
            return -1
        return length