class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product= [1]*(len(nums))
        suffix_product= [1]*len(nums)
        result= []
        for i in range(len(nums)): 
            if i==0: 
                prefix_value=1 
                prefix_product[i]=1
            else: 
                prefix_product[i]=prefix_product[i-1] * nums[i-1]
        
        for i in range(len(nums)-1,-1,-1): 
            if(i==len(nums)-1): 
                suffix_product[i]=1
            else: 
                suffix_product[i]=suffix_product[i+1] * nums[i+1]

        for j in range (len(nums)): 
            result.append(prefix_product[j]*suffix_product[j])
        return result 