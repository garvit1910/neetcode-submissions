class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq= {}
        result=[]
        visited= set ()
        cycle= set ()
        for i in range(numCourses): 
            prereq[i]=[ ]

        for crs, pre in prerequisites: 
            prereq[crs].append(pre)
        def dfs(node): 

            if node in cycle: 
                return False 
            if node in visited: 
                return True 
            
            cycle.add(node)
            for pre in prereq[node]: 
                if dfs(pre)==False: 
                    return False 
            cycle.remove(node)
            visited.add(node)
            result.append(node)
            return True 
            
        for c in range(numCourses): 
            if dfs(c)==False: 
                return []
        return result

        