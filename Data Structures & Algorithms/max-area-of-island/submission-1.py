class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROW = len(grid)
        COLUMN=len(grid[0])
        visit=set()
        maxarea=0
        def dfs(grid, r,c,visit): 
            count=0 
            if min(r,c) < 0 or r==ROW or c==COLUMN or (r,c) in visit or grid[r][c]==0: 
                return 0
            visit.add((r,c))
            count+=1 
            count+=dfs(grid, r+1, c, visit) + dfs(grid, r-1, c, visit) + dfs(grid, r, c+1, visit) + dfs(grid, r, c-1, visit)
            return count

        
        for i in range(ROW): 
            for j in range(COLUMN): 
                if grid[i][j]==1 and (i,j) not in visit: 
                    maxarea=max(maxarea,dfs(grid, i, j, visit))
        return maxarea

        dfs(grid, 0,0,set())
