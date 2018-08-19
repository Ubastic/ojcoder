class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        sub = ''
        count = 0
        for c in s:
            if c in '0123456789':
                count = count * 10 + int(c)
            elif c == '[':
                stack.append((count, sub))
                count = 0
                sub = ''
            elif c == ']':
                inner = sub
                count, sub = stack.pop()
                sub += inner * count
                count = 0
            else:       # c is letter
                sub += c
        return sub