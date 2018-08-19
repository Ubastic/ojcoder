class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        groups = dict()
        for s in strings:
            key = self.generateKey(s)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        return groups.values()
        
    def generateKey(self, string):
        diffs = []
        for i in xrange(len(string)):
            diff = (ord(string[i]) - ord(string[i-1])) % 26
            diffs.append(str(diff))
        return ''.join(diffs)