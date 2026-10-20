class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        pass

        ROW, COLUMN=len(grid), len(grid[0])
        visited=set ()
        maximum=0
        def dfs(r,c, grid): 
            total=0
            if r==ROW or c==COLUMN or min(r,c) < 0 or (r,c) in visited or grid[r][c]==0:
                   return 0

            visited.add((r,c))
            total+= grid[r][c] + dfs(r+1, c, grid) + dfs(r-1,c,grid) + dfs(r,c+1, grid) + dfs(r, c-1, grid)
            return total
        

        for i in range(ROW): 
            for j in range(COLUMN): 
                if grid[i][j]!=0 and (i,j) not in visited: 
                    maximum=max(maximum, dfs(i,j,grid))
        return maximum