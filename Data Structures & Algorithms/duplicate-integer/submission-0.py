class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    
        nums_seen= set ( )
        for i in nums: 
            if i not in nums_seen: 
                nums_seen.add(i) 
            else: 
                return True
        
        return False
