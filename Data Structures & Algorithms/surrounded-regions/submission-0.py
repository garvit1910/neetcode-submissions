class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROW, COLUMN= len(board), len(board[0]) 
        visit=set( )
        def dfs(board, r, c, visit): 

            

            if(min(r,c) < 0 or r==ROW or c==COLUMN or board[r][c]=="X" or (r,c) in visit): 
                    return


            if board[r][c]=="O" and (r==0 or r==ROW-1 or c==0 or c==COLUMN-1): 
                visit.add((r,c))
                dfs(board, r+1, c, visit)
                dfs(board, r-1, c, visit)
                dfs(board, r, c+1, visit) 
                dfs(board, r, c-1, visit) 

            visit.add((r,c))
        
            dfs(board, r+1, c, visit)
            dfs(board, r-1, c, visit)
            dfs(board, r, c+1, visit)
            dfs(board, r, c-1, visit)

        for i in range(1): 
            for j in range(COLUMN): 
                dfs(board, i, j, visit)
        
        for i in range(ROW-1, ROW): 
            for j in range(COLUMN): 
                dfs(board, i, j, visit)
        
         
        for i in range(ROW): 
            for j in range(1): 
                dfs(board, i, j, visit)
         
        for i in range(ROW): 
            for j in range(COLUMN-1, COLUMN): 
                dfs(board, i, j, visit)
            
        
        for i in range(ROW): 
            for j in range(COLUMN): 
                if board[i][j]=="O" and (i,j) not in visit:
                    board[i][j]="X"
                dfs(board, i, j, visit)

            