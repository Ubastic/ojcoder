class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = s.split()
        slist = map(lambda x:x[::-1], slist)
        return ' '.join(slist)