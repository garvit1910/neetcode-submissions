from collections import deque 
class Solution:
 def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    queue=deque() 
    visited= set ()
    ROW,COLUMN= len(grid), len(grid[0])
    count=float('inf')

    for i in range(ROW): 
        for j in range(COLUMN): 
            if grid[i][j]==0: 
                queue.append((i,j))
                visited.add((i,j))
    
    while queue: 
        r,c= queue.popleft()
        directions=[[1,0],[-1,0],[0,1],[0,-1]] 
        for dr, dc in directions: 
            nr, nc= r + dr, c+dc
            if(nr==ROW or nc==COLUMN or min(nr,nc) < 0 or (nr,nc) in visited or grid[nr][nc]==-1):
                continue 
            visited.add((nr,nc))
            queue.append((nr,nc))
            grid[nr][nc]=grid[r][c] + 1
            




