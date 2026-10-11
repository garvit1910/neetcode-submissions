from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        result= []
        for i in strs: 
            arr= [0] * 26
            for c in i: 
                arr[ord(c)-ord('a')]+=1 
            hashmap[tuple(arr)].append(i)

        for keys,values, in hashmap.items(): 
            result.append(values)

        return result

    
    
    