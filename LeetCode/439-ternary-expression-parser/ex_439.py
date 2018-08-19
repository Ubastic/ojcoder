class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if len(expression) == 1:    return expression
        idx = self.findSplitIndex(expression)
        if expression[0] == 'T':
            return self.parseTernary(expression[2:idx])
        else:
            return self.parseTernary(expression[idx+1:])
    
    def findSplitIndex(self, exp):
        count = -1
        i = 2
        while i < len(exp):
            if exp[i] == '?':
                count -= 1
            elif exp[i] == ':':
                count += 1
                if count == 0:  break
            i += 1
        return i