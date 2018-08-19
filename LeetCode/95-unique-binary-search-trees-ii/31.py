# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:  return []
        return self.generate(1, n)
        
    def generate(self, start, end):
        if start > end: return [None]
        res = []
        for i in range(start, end+1):
            left = self.generate(start, i-1)
            right = self.generate(i+1, end)
            for l in left:
                for r in right:
                    n = TreeNode(i)
                    n.left = l
                    n.right = r
                    res.append(n)
        return res