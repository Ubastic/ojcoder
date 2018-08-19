# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        l, r = float('-inf'), float('inf')
        node = root
        while node:
            if target > node.val:
                l = node.val
                node = node.right
            else:
                r = node.val
                node = node.left
        return l if abs(l - target) < abs(r - target) else r