class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result= [ ]
        nums=sorted(nums)
        for i in range(len(nums)):
            L,R = i+1, len(nums)-1
            while L < R: 
                if(nums[L]+nums[R]+nums[i] < 0): 
                    L+=1 
                elif(nums[L]+nums[R]+nums[i] > 0): 
                    R-=1 
                elif (nums[L]+nums[R]+nums[i] == 0):
                        if sorted([nums[L],nums[R],nums[i]]) not in result:
                            result.append(sorted([nums[L],nums[R],nums[i]]))
                        L+=1 
                        R-=1 
        return result                 
    
            