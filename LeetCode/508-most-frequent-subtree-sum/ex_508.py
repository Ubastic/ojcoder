# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:    return []
        counter = {}
        self.helper(root, counter)
        max_freq = max(counter.values())
        res = []
        for k in counter:
            if counter[k] == max_freq:
                res.append(k)
        return res
        
    def helper(self, root, counter):
        if not root:    return  0
        tree_sum = root.val + self.helper(root.left, counter) + self.helper(root.right, counter)
        if tree_sum in counter:
            counter[tree_sum] += 1
        else:
            counter[tree_sum] = 1
        return tree_sum
        