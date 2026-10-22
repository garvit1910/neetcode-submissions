class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
    
        adjlist= {}
        candidates=[ ]
        for i in range(1,n+1): 
            adjlist[i]=[ ]
    
        for src, dst in trust: 
            adjlist[src].append(dst)
    
        for person, trusted_person in adjlist.items(): 
            if adjlist[person]==[]: 
                candidates.append(person)
        
        
        for candidate in candidates:
            counter=0
            for person in adjlist: 
                if candidate in adjlist[person]: 
                    counter+=1 
        
            if(counter==n-1): 
                    return candidate
    
        return -1