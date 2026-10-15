# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth=0
        curr=root 
        if curr is None: 
            return depth
        depth+=1 
        depth+=max(self.maxDepth(curr.left), self.maxDepth(curr.right))
        return depth
        
