class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums= sorted(nums)
        chain_length=1
        result= [ ]
        if(nums==[]): 
            return 0
        for i in range(len(nums)):
            if(i==len(nums)-1): 
                result.append(chain_length)
                break
            if(nums[i+1]-nums[i]==1):
                chain_length+=1 
            elif(nums[i+1]-nums[i]==0): 
                continue
            else: 
                result.append(chain_length)
                chain_length=1   
        return max(result)