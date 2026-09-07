# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque()
        queue.append(root)

        level = -1

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node:
                    queue.append(node.right)
                    queue.append(node.left)
            level += 1

        return level