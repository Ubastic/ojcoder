class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ret = []
        for i in xrange(1024):
            if bin(i).count('1') == num:
                h = i >> 6
                m = i & 0x3f
                if h < 12 and m < 60:
                    ret.append("%d:%02d" % (h, m))
        return ret