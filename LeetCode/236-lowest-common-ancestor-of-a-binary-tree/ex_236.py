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
        nums, nodes = self.LCA_helper(root, p ,q)
        return nodes
    
    def LCA_helper(self, root, p, q):
        if not root:    return (0, None)
        lcount, node = self.LCA_helper(root.left, p, q)
        if lcount == 2:     # if both nodes are descendants of the left child
            return (lcount, node)
        rcount, node = self.LCA_helper(root.right, p, q)
        if rcount == 2:     # if both nodes are descendants of the right child
            return (rcount, node)
        nodes_cnt = lcount + rcount + int(root == p) + int(root == q)
        if nodes_cnt == 2:  # root is the ancestor
            return (nodes_cnt, root)
        return (nodes_cnt, None)    # not found