# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        table = {}
        self.helper(root, table, 0, 0)
        res = []
        for h in sorted(table):
            col = []
            for v in sorted(table[h]):
                col.extend(table[h][v])
            res.append(col)
        return res
        
    def helper(self, node, table, v, h):
        if not node:    return
        if h not in table:
            table[h] = {}
        if v not in table[h]:
            table[h][v] = []
        table[h][v].append(node.val)
        self.helper(node.left, table, v+1, h-1)
        self.helper(node.right, table, v+1, h+1)
        