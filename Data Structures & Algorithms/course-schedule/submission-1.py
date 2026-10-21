class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=set ()
        premap = {}
        for i in range(numCourses): 
            premap[i]=[ ]

        for crs,pre in prerequisites: 
            premap[crs].append(pre)
    
        def dfs(crs): 
            if premap[crs]==[]: 
                return True
            if crs in visited: 
                return False 
        
            visited.add(crs)

            for pre in premap[crs]: 
                if not dfs(pre): 
                    return False 
            visited.remove(crs)
            premap[crs]=[] 
            return True

        for course in range(numCourses): 
            if not dfs(course): 
                return False 
        return True 
    

    
