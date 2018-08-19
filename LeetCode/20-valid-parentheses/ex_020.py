class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = [('(', ')'), ('[', ']'), ('{', '}')]
        for c in s:
            if c in '([{':
                stack.append(c)
            elif not stack:
                return False
            else:
                for l, r in pairs:
                    if c == r and stack.pop() != l:
                        return False
        return not stack