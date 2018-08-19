# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    max_path = float('-inf')
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_path = float('-inf')
        self.helper(root)
        return self.max_path
        
    def helper(self, node):
        if not node:    return 0
        max_left = self.helper(node.left)
        max_right = self.helper(node.right)
        if max_left < 0:    max_left = 0        # if left < 0, no contributions to maximun, reset
        if max_right < 0:   max_right = 0       # same
        self.max_path = max(self.max_path, max_left + max_right + node.val)
        max_t = node.val + max(max_left, max_right)
        return max_t
        