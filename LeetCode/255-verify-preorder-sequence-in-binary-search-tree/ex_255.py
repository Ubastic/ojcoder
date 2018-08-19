class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if not preorder:    return True
        stack = []
        low = float('-inf')
        for n in preorder:
            if n < low:
                return False
            while stack and stack[-1] < n:
                low = stack.pop()
            stack.append(n)
        return True