class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit=set ()
        ROW,COLUMN=len(grid), len(grid[0])
        count=0
        def dfs(grid,r,c,visit): 
            if (min(r,c) < 0 or r==ROW or c==COLUMN or (r,c) in visit or grid[r][c]=="0"):
                return 

            visit.add((r,c))

            dfs(grid, r, c+1, visit)
            dfs(grid, r, c-1, visit)
            dfs(grid, r-1, c, visit)
            dfs(grid, r+1, c, visit)
        count=0
        for rows in range(ROW):
            for col in range(COLUMN): 
                if grid[rows][col]=="1" and (rows,col) not in visit:
                    count+=1 
                    dfs(grid, rows, col, visit)
        return count 
               
        dfs(grid, 0,0,visit)

         