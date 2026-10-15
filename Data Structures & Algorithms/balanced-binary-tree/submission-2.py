# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        curr=root
        if curr is None: 
            return True

        if( -1 <= self.maxheight(curr.left)-self.maxheight(curr.right) <=1): 
            return self.isBalanced(curr.left) and self.isBalanced(curr.right)
            
        else: 
            return False
        return True


    

    def maxheight(self, root: Optional[TreeNode]) -> int: 
        height=0 
        curr=root 
        if curr is None:
            return height 
        height+=1 
        height+= max(self.maxheight(curr.left),self.maxheight(curr.right))
        return height 
