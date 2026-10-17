class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COLUMN= len(grid), len(grid[0])
        visit=set ()
        count=0
        def dfs(grid, r, c, visit): 
            if r==ROW or c==COLUMN or min(r,c) < 0 or (r,c) in visit or grid[r][c]=="0": 
                return 
            
            visit.add((r,c))

            dfs(grid, r+1, c, visit)
            dfs(grid, r-1, c, visit)
            dfs(grid, r, c-1, visit)
            dfs(grid, r, c+1, visit)
        
        for i in range(ROW): 
            for j in range(COLUMN): 
                if grid[i][j]=="1" and (i,j) not in visit:
                    count+=1 
                    dfs(grid, i,j,visit)
        return count

        dfs(grid,0,0,set())
      