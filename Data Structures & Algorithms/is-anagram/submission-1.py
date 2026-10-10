from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1= defaultdict(int)
        for value in s: 
            d1[value]+=1 
        for value in t:  
            if d1.get(value)==None: 
                return False 
            if(d1[value] > 0 and len(t)==len(s)): 
                d1[value]-=1 
            else: 
                return False 
        return True