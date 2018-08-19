# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[0]
        
    def helper(self, node):
        if not node:    return (0, None, True)
        if not node.left and not node.right:    return (1, node.val, True)
        left = self.helper(node.left)
        right = self.helper(node.right)
        if left[2] and right[2] and                         \
            (left[1] == node.val or left[1] == None) and    \
            (right[1] == node.val or right[1] == None):
            return (left[0] + right[0] + 1, node.val, True)
        else:
            return (left[0] + right[0], node.val, False)