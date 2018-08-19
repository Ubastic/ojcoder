class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        length = len(num) - k
        for c in num:
            while k and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
        return ''.join(stack[:length]).lstrip('0') or '0'