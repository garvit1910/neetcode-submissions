from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited=set()
        queue=deque()
        ROW, COLUMN= len(grid), len(grid[0]) 
        timer=0
        fresh=0
        for i in range(ROW): 
            for j in range(COLUMN): 
                if grid[i][j]==2: 
                    queue.append((i,j))
                    visited.add((i,j))
                elif grid[i][j]==1: 
                    fresh+=1 
        if fresh==0: 
            return 0
        
        while queue: 
            rotted=False
            for i in range(len(queue)): 
                r,c = queue.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions: 
                    nr, nc= r+dr, c+dc 
                    if min(nr,nc) < 0 or nr==ROW or nc==COLUMN or grid[nr][nc]==0 or (nr,nc) in visited:
                        continue 
                    grid[nr][nc]=2
                    rotted=True 
                    fresh-=1 
                    visited.add((nr,nc))
                    queue.append((nr,nc))
            if rotted: 
                timer+=1 
        for i in range(ROW): 
            for j in range(COLUMN): 
                if fresh > 0:
                    return -1 


        return timer

    