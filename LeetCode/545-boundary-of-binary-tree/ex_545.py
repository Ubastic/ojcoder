# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:    return []
        seen = set()
        lb = self.left_boundary(seen, root)
        rb = self.right_boundary(seen, root)
        middle = []
        self.get_middle(seen, root, middle)
        return lb + middle + rb
        
        
    def left_boundary(self, seen, root):
        res = []
        p = root
        while p:
            if p not in seen:
                res.append(p.val)
                seen.add(p)
            if p.left:
                p = p.left
            elif p == root:
                break
            else:
                p = p.right
        return res
        
    def right_boundary(self, seen, root):
        res = []
        p = root
        while p:
            if p not in seen:
                res.append(p.val)
                seen.add(p)
            if p.right:
                p = p.right
            elif p == root:
                break
            else:
                p = p.left
        return res[::-1]
        
    def get_middle(self, seen, root, middle):
        if not root:    return
        if not root.left and not root.right:
            if root not in seen:
                middle.append(root.val)
        self.get_middle(seen, root.left, middle)
        self.get_middle(seen, root.right, middle)