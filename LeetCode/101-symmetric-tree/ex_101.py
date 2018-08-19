# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_symmetric(l, r):
            if not l and not r:
                return True
            elif (l and r):
                return l.val == r.val and check_symmetric(l.left, r.right) and check_symmetric(r.left, l.right)
            else:
                return False
        return not root or check_symmetric(root.left, root.right)