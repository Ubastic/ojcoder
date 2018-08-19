# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[0]
    
    def helper(self, node):
        if not node:    return 0, 0, float('inf'), float('-inf')    # largest BST tree, number of nodes, min val, max val
        left = self.helper(node.left)
        right = self.helper(node.right)
        if node.val > left[3] and node.val < right[2]:
            n = left[1] + right[1] + 1
        else:
            n = float('-inf')
        return max(n, left[0], right[0]), n, min(left[2], node.val), max(right[3], node.val)
        