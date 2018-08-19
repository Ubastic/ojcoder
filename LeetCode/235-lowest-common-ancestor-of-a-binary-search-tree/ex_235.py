# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        s = p if p.val <= q.val else q
        b = q if q.val > p.val else p
        ca = root
        while (ca.val < s.val or ca.val > b.val):
            while (ca.val < s.val):
                ca = ca.right
            while (ca.val > b.val):
                ca = ca.left
        return ca