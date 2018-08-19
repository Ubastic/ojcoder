# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, prev):
            if not root:
                return 0
            if not root.left and not root.right:
                return prev * 10 + root.val
            num = prev * 10 + root.val
            ans = 0
            if root.left:
                ans += helper(root.left, num)
            if root.right:
                ans += helper(root.right, num)
            return ans
        return helper(root, 0)