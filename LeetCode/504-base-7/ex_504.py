class Solution(object):
    def convertTo7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        is_positive = True
        if num < 0:
            is_positive = False
            num = -num
        res = []
        while num:
            res.append(str(num % 7))
            num = num / 7
        return ''.join(reversed(res)) if is_positive else '-' + ''.join(reversed(res))