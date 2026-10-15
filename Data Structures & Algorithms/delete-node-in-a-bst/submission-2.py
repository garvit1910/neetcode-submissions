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
            curr.left=self.deleteNode(curr.left, key) #connecting edges and following
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
                curr.right= self.deleteNode(curr.right, minNode.val) #removing the duplicate lowest number from the rest of thr graph 
                
        return root

# there are two cases to remove, either the node being removed has 2 children 
# or the node being removed doesnt have any subtrees either on left, right 
# or both. we are finding the smallest value in the right subtree, since we 
#know it's going to be the smallest value, and rest of the tree is going to 
#still obey property of bst. 

    def findmin(self, root: Optional[Treenode]) -> Optional[Treenode]: 
        curr=root
        while curr.left: 
            curr=curr.left 
        return curr
        
        