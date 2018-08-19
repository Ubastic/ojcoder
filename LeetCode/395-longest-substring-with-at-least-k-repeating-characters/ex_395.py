class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = collections.Counter(s)
        filters = [x for x in cnt if cnt[x] < k]
        if not filters:
            return len(s)
        sub = re.split("|".join(filters), s)
        return max(self.longestSubstring(t, k) for t in sub)