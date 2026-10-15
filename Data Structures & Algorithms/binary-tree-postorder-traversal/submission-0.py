# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result= [ ]
        curr=root
        if curr is None: 
            return []
        result+=self.postorderTraversal(curr.left)
        result+=self.postorderTraversal(curr.right)
        result.append(curr.val)

        return result

