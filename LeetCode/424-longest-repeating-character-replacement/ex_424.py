class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = [0] * 26
        res = char_count = start = end = 0
        while end < len(s):
            count[ord(s[end]) - ord('A')] += 1
            char_count = max(char_count, count[ord(s[end]) - ord('A')])
            end += 1
            while end - start - char_count > k:
                count[ord(s[start]) - ord('A')] -= 1
                start += 1
                char_count = max(count + [char_count])
            res = max(end - start, res)
        return res