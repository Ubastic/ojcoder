class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) -1
        j = len(num2) -1
        carry = 0
        res = ''
        
        while i >= 0 or j >= 0 or carry > 0:
            s = 0
            if i >= 0:
                s += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                s += ord(num2[j]) - ord('0')
                j -= 1
            s += carry
            carry = s / 10
            s %= 10
            res = str(s) + res
            
        return res
