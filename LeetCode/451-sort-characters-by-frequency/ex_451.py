class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        heap = []
        res = []
        char_count = collections.Counter(s)
        for c in char_count:
            t = (-char_count[c], c)
            for i in xrange(-t[0]):
                heapq.heappush(heap, t)
        while heap:
            res.append(heapq.heappop(heap)[1])
        return "".join(res)