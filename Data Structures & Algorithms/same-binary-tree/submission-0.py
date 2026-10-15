# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        curr1= p 
        curr2= q 

        if curr1 is None and curr2 is None:
            return True
        elif curr1 is None or curr2 is None:
            return False
        if(curr1.val==curr2.val): 
            return self.isSameTree(curr1.left, curr2.left) and self.isSameTree(curr1.right, curr2.right)
        else: 
            return False