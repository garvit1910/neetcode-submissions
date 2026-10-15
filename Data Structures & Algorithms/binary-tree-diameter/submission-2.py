# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0 
        curr=root
        if curr is None:
            return diameter
        diameter=self.maxheight(curr.left)+self.maxheight(curr.right)
        return max(diameter, self.diameterOfBinaryTree(curr.left), self.diameterOfBinaryTree(curr.right))




    def maxheight(self, root: Optional[TreeNode])-> int: 
        curr=root 
        height=0 
        if curr is None: 
            return height 
        height+=1 
        height+=max(self.maxheight(curr.left), self.maxheight(curr.right))
        return height

