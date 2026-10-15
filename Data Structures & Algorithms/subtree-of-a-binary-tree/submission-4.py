# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        curr=root
        if curr is None and subRoot is None: 
            return True 
        elif curr is None or subRoot is None: 
            return False
        if(curr.val==subRoot.val): 
            return self.isSame(curr, subRoot) or self.isSubtree(curr.left, subRoot) or self.isSubtree(curr.right, subRoot)
        else:
            return self.isSubtree(curr.left, subRoot) or self.isSubtree(curr.right, subRoot)
        return False


        
    




    def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode])->bool:
        curr1=p
        curr2=q 
        if curr1 is None and curr2 is None: 
            return True 
        elif curr1 is None or curr2 is None: 
            return False 
        
        if(curr1.val==curr2.val): 
            return self.isSame(curr1.left, curr2.left) and self.isSame(curr1.right, curr2.right)
        else: 
            return False












