# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    last = -1
    diff = 0x7FFFFFFF
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:    return self.diff
        self.getMinimumDifference(root.left)
        if self.last != -1:
            self.diff = min(self.diff, root.val - self.last)
        self.last = root.val
        self.getMinimumDifference(root.right)
        return self.diff