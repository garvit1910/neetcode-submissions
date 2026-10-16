# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inordertraversal(root,k):
            result=[ ]
            curr=root
            if curr is None: 
                return []
            result+= inordertraversal(curr.left, k)
            result.append(curr.val)
            result+= inordertraversal(curr.right, k)
            return result 
        return inordertraversal(root,k)[k-1]
        