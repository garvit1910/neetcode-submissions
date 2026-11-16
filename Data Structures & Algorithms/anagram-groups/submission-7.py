class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        visited= defaultdict(list)
        result=[]

        for i in range(len(strs)):
            if (tuple(sorted(strs[i]))) not in visited: 
                visited[tuple(sorted(strs[i]))]=[strs[i]]
            else: 
                visited[tuple(sorted(strs[i]))].append(strs[i])
        
        for k,v in visited.items(): 
            result.append(v)
        
        return result

            
          



        