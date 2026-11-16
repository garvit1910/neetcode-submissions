class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        A=[]
        for idx, val in enumerate(nums): 
            A.append([idx, val])

        A.sort(key=lambda x: x[1])

        L, R= 0, len(A)-1 

        while L < R: 
            if A[L][1]+A[R][1]==target: 
                return [min(A[L][0], A[R][0]), max(A[L][0], A[R][0])] 
            
            elif A[L][1]+A[R][1] < target: 
                L=L+1 
            
            elif A[L][1] + A[R][1] > target: 
                R=R-1 
            

        