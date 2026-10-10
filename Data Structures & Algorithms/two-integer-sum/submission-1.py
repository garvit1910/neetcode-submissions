class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap= { }
        
        for i in range(len(nums)):  
            target2= target-nums[i] 
            if target2 in hashmap: 
                return [hashmap[target2],i]
            else: 
                hashmap[nums[i]]=i



