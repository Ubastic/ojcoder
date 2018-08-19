class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        stats = [0] * (len(citations) + 1)
        for i in citations:
            stats[min(i, len(citations))] += 1
        count = 0
        for i in range(len(citations), -1, -1):
            count += stats[i]
            if count >= i:
                return i
        return 0