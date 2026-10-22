class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList={}
        cycle= set ()
        for i in range(n): 
            adjList[i]=[ ] 
        
        for src, dst in edges: 
            adjList[src].append(dst)
            adjList[dst].append(src)
        
        def dfs(node, parent): 
            if node in cycle: 
                return False 
            cycle.add(node)
            for neighbor in adjList[node]:
                if neighbor==parent:
                    continue 
                if dfs(neighbor, node)==False: 
                    return False 

            return True
        
        if not dfs(0,-1): 
            return False 
        
        return len(cycle)==n
        