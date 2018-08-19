# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:    return res
        curr = [root]
        while curr:
            level_max = float('-inf')
            next_level = []
            for node in curr:
                level_max = max(level_max, node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(level_max)
            curr = next_level
        return res
        