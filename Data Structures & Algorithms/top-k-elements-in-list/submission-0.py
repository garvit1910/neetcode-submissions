from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict_nums=defaultdict(int)
        for i in nums: 
            dict_nums[i]+=1  #dict with nums as keys, count as values
        
        dict_nums= sorted(dict_nums.items(), key=lambda v: v[1],reverse=True) 

        result= [ ]
        for keys,values in dict_nums: 
            if( k > 0): 
                result.append(keys)
                k-=1 

        return result 