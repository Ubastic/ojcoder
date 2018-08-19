# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        lst = []
        def paths(node, lst, sub_path = ""):
            if not node:    return
            new_path = sub_path + str(node.val)
            if not node.left and not node.right:
                lst.append(new_path)
                return
            new_path += "->"
            paths(node.left, lst, new_path)
            paths(node.right, lst, new_path)
        paths(root, lst)
        return lst