class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        copy = num
        i = 0
        while copy != 0:
            copy >>= 1
            num ^= (1 << i)
            i += 1
        return num