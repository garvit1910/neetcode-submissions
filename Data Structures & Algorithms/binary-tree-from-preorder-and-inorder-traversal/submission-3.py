# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index={}

        for i, val in enumerate(inorder): 
            inorder_index[val]=i 
        preorder_idx=0

        def build(left, right): 
            nonlocal preorder_idx
            if left > right: 
                return None 
            root_val=preorder[preorder_idx]
            preorder_idx+=1 

            root=TreeNode(root_val)

            i=inorder_index[root_val]

            root.left=build(left, i-1)
            root.right=build(i+1, right)

            return root 
        return build(0, len(inorder)-1)

            


        