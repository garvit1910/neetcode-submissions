class Solution:

    def encode(self, strs: List[str]) -> str:
     s2= ""
     for s in strs: 
        s1= f"{str(len(s))}#{s}"
        s2+=s1
     return s2
##"5#hello"
    def decode(self, s: str) -> List[str]:
        result= [ ]
        i=0 
        while i < len(s):
            j=i
            while s[j]!= "#": 
                j+=1 
            char_count= int(s[i:j])
            word=""
            for k in range(j+1, j+1+char_count):
                    word+=s[k] 
            result.append(word)
            i=j+1+char_count
        return result 





        