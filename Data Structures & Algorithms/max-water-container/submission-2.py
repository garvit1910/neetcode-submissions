class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L,R = 0,len(heights)-1 
        result=0 
        while L < R: 
            area= (R-L)* min(heights[L],heights[R])
            result=max(area,result)
            if(heights[L] <= heights[R]): 
                L+=1 
            elif(heights[R] < heights[L]): 
                R-=1 

        return result
            


