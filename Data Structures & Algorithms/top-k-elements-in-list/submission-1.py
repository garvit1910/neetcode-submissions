class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap={}
        result=[]

        for i in range(len(nums)): 
            if nums[i] in hashmap: 
                hashmap[nums[i]]+=1 
            
            else:
                hashmap[nums[i]]=1 
        

        hashmap= sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
     

        for i in range(k): 
            result.append(hashmap[i][0])
        
        return result