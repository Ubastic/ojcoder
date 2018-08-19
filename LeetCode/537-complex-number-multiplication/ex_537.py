class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ar, ai = map(int, a.strip('i').split('+'))
        br, bi = map(int, b.strip('i').split('+'))
        rr = ar * br - ai * bi
        ri = ar * bi + ai * br
        return '' + str(rr) + '+' + str(ri) + 'i'