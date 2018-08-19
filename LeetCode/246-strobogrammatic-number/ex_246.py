class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for c in num:
            if c in '23457':
                return False
        nmap = {'6':'9', '9':'6', '0':'0', '1':'1', '8':'8'}
        i = 0
        j = len(num) - 1
        while i <= j:
            if nmap[num[i]] != num[j]:
                return False
            i += 1
            j -= 1
        return True