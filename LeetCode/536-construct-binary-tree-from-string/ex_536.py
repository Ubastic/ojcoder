# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:   return None
        idx = s.find('(')
        if idx == -1:    return TreeNode(int(s))
        
        node = TreeNode(int(s[:idx]))
        
        count = 1
        i = idx + 1
        while count:
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
            i += 1
            
        node.left = self.str2tree(s[idx+1:i-1])
        if i != len(s): node.right = self.str2tree(s[i+1:-1])
        return node