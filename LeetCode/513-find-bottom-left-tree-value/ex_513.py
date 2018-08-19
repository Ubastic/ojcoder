# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeftMostNode(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)[0]
        
    def helper(self, node, depth):
        if not node:    return (-1, -1)
        left, h = node.val, depth
        lleft, lh = self.helper(node.left, depth + 1)
        rleft, rh = self.helper(node.right, depth + 1)
        
        if h > lh and h > rh:
            return left, h
        elif rh > h and rh > lh:
            return rleft, rh
        else:
            return lleft, lh