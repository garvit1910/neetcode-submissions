# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #return pair: [withRoot, withoutRoot]
        def dfs(node): 
            if node is None: 
                return [0,0]
            leftpair=dfs(node.left)
            rightpair=dfs(node.right)

            withRoot= node.val + leftpair[1] + rightpair[1]

            #if root is included, we need to add it with the case 

            #where we did not INCLUDE the children of the node 

            withoutRoot= max(leftpair) + max(rightpair)

            return [withRoot, withoutRoot]
        
        return max(dfs(root))

        

