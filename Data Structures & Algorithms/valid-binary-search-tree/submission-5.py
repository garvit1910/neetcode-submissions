# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, minval, maxval): 
          if node is None: 
            return True
          if (minval < node.val < maxval): 
           return dfs(node.left, minval, node.val) and dfs(node.right, node.val, maxval)
          return False
        
        return dfs(root.left, float("-inf"), root.val) and dfs(root.right, root.val, float("inf"))