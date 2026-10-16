# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
       
     
       def dfs(node, maxval): 
            counter=0
            if node is None: 
                return 0
            
            if node.val >= maxval: 
                counter=1 
                maxval=node.val 
            counter+=dfs(node.left, maxval) + dfs(node.right, maxval)
            return counter 
       return dfs(root.left, root.val) + dfs(root.right, root.val) + 1

