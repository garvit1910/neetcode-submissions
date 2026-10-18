class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COLS=len(heights),len(heights[0])
        pacific= set ()
        atlantic= set ()

        def dfs(r, c, visit, prevheight): 
            if(min(r,c) < 0 or r==ROW or c==COLS or (r,c) in visit or heights[r][c] < prevheight): 
                return 
    
            visit.add((r,c))

            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])


        for r in range(ROW):
            dfs(r,0,pacific, heights[r][0])
            dfs(r,COLS-1, atlantic, heights[r][COLS-1])
        
        for c in range(COLS): 
            dfs(0,c, pacific, heights[0][c])
            dfs(ROW-1,c, atlantic, heights[ROW-1][c])

        result=[ ]
        for i in range(ROW): 
            for j in range(COLS): 
                if (i,j) in pacific and (i,j) in atlantic: 
                    result.append([i,j])
        return result



             
