# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    max_val = 0
    
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_val = 0
        self.helper(root)
        return self.max_val
        
    def helper(self, node):
        if not node:    return 0, 0     # inc, dec
        inc, dec = 1, 1
        
        if node.left:
            left_inc, left_dec = self.helper(node.left)
            if node.val == node.left.val + 1:
                dec = left_dec + 1
            elif node.val == node.left.val - 1:
                inc = left_inc + 1
        
        if node.right:
            right_inc, right_dec = self.helper(node.right)
            if node.val == node.right.val + 1:
                dec = max(dec, right_dec + 1)
            elif node.val == node.right.val - 1:
                inc = max(inc, right_inc + 1)
                
        self.max_val = max(self.max_val, dec + inc - 1)
        
        return inc, dec