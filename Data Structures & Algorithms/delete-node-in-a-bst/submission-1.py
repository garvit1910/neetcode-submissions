# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr=root
        if curr is None: 
            return 
        if key < curr.val: 
            curr.left=self.deleteNode(curr.left, key)
        elif key > curr.val: 
            curr.right= self.deleteNode(curr.right, key)
        else: 
            if curr.left is None: 
                return curr.right 
            elif curr.right is None: 
                return curr.left  
            else: 
                minNode=self.findmin(curr.right)
                curr.val=minNode.val 
                curr.right= self.deleteNode(curr.right, minNode.val)
                
        return root

    def findmin(self, root: Optional[Treenode]) -> Optional[Treenode]: 
        curr=root
        while curr.left: 
            curr=curr.left 
        return curr
        
        