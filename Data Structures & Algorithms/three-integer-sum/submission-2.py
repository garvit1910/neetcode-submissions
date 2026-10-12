class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = [ ]
        seen = set ( )
        nums.sort( )
        for i in range(len(nums)): 
            L,R=i+1, len(nums)-1
            while L < R: 
                if(nums[i]+ nums[L]+nums[R] > 0): 
                    R-=1 
                elif(nums[i]+ nums[L]+nums[R] < 0): 
                    L+=1 
                else: 
                    triplet= (nums[i],nums[L],nums[R]) 
                    if triplet not in seen: 
                        result.append(list(triplet))
                        seen.add(triplet)
                    L+=1 
                    R-=1 
        return result

