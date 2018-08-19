# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:    return []
        level = [root]
        res = []
        reverse = False
        while level:
            l = [node.val for node in level]
            if reverse:
                res.append(l[::-1])
            else:
                res.append(l)
            reverse = not reverse
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return res
            