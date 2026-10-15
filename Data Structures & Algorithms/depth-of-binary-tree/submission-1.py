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
            #this will always return 0 because when a function is being called 
            #depth is always initialised to 0 in the start. 
        depth+=1 
        #every time a node exists, make the counter increase by 1. 
        depth+=max(self.maxDepth(curr.left), self.maxDepth(curr.right))
        #i am finding the max length in each subtree using this 
        return depth
        
