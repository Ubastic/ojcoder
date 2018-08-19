# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s = []
        self.helper(s, root)
        count = collections.Counter(s)
        freq = max(count.values())
        return [c for c in count if count[c] == freq]
        
    def helper(self, s, root):
        if not root:    return
        s.append(root.val)
        self.helper(s, root.left)
        self.helper(s, root.right)