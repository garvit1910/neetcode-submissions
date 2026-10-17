class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        
        original_colour= image[sr][sc]
        def dfs(image, r, c, color, visit): 
            m,n = len(image), len(image[0])
            if r==m or c==n or (min(r,c) < 0) or image[r][c]!=original_colour or (r,c) in visit: 
                return 
            visit.add((r,c))
            if image[r][c]==original_colour: 
                image[r][c]=color 
            dfs(image, r+1, c, color, visit)
            dfs(image, r, c+1, color, visit) 
            dfs(image, r-1, c, color, visit)
            dfs(image, r, c-1, color, visit)


        dfs(image, sr, sc, color,set ())
    
        return image