# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.count = 0 
    
        def inorder(node):
            if not node:
                return None

            left_res = inorder(node.left)
            if left_res is not None: 
                return left_res 

 
            self.count += 1
            if self.count == k:
                return node.val

            return inorder(node.right)
        return inorder(root)