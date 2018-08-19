# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:    return 0
        return self.helper(root, root.val - 1, 0)
        
    def helper(self, node, parent_val, count):
        if not node:    return count
        if node.val != parent_val + 1:  count = 0
        count += 1
        return max(self.helper(node.left, node.val, count), self.helper(node.right, node.val, count), count)