class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset= set ( )
        L, R = 0, 0 
        maxlength=0

        if s is None: 
            return 0
        elif len(s)==1: 
            return 1
        while R < len(s): 
            if s[R] not in charset:  
                charset.add(s[R])
                maxlength=max(R-L+1, maxlength)
                R+=1 
            else: 
                    charset.remove(s[L])
                    L+=1 
                
        return maxlength

                



            
