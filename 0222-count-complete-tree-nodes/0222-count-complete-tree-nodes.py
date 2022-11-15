# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def left_height(root):
            
            ht = 0
            while(root):
                ht+=1
                root = root.left
            return ht
        def right_height(root):
            
            ht = 0
            while(root):
                ht+=1
                root = root.right
            return ht
        def total_nodes(root):
            
            if root == None:
                return 0
            lh = left_height(root)
            rh = right_height(root)
            
            if (lh == rh):
                return (1 << lh)-1
            else:
                return 1 + total_nodes(root.left) + total_nodes(root.right)
            
        return total_nodes(root)