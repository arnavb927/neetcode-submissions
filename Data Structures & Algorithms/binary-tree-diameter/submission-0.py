# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def max_height(root):
            if root == None:
                return 0

            return 1 + max(max_height(root.left), max_height(root.right))

        if root == None:
            return 0
        
        right = max_height(root.right)
        left = max_height(root.left)
        total = right + left
        res = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), total)
        return res


        



        
        
        

        