# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def max_h(root):
            if not root:
                return 0
            
            return 1 + max(max_h(root.right), max_h(root.left))


        stack = [[root, max_h(root.right) + max_h(root.left)]]
        res = 0

        while stack:
            node, dia = stack.pop()
            res = max(res, dia)
            if node.right:
                node_r = node.right
                stack.append([node_r, max_h(node_r.right) + max_h(node_r.left)])
                
            if node.left:
                node_l = node.left
                stack.append([node_l, max_h(node_l.left) + max_h(node_l.right)])
        
        return res





        



        
        
        

        