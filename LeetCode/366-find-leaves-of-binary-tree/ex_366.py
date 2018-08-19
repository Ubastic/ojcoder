# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.height(res, root)
        return res
    
    def height(self, res, root):
        if not root:    return -1
        level = 1 + max(self.height(res, root.left), self.height(res, root.right))
        if len(res) < level + 1:    res.append([])
        res[level].append(root.val)
        return level
            