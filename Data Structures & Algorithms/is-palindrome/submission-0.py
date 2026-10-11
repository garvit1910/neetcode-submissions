class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for c in s: 
            if c.isalnum(): 
                s1+=c.lower()
        L,R=0,len(s1)-1
        for c in s:
         while L < R: 
            if(s1[L]==s1[R]): 
                L+=1 
                R-=1 
            else: 
                return False
        return True