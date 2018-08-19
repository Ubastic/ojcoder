class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = collections.Counter()
        chars = set()
        res = i = j = 0
        while j < len(s):
            chars.add(s[j])
            counter[s[j]] += 1
            j += 1
            while len(chars) > 2:
                counter[s[i]] -= 1
                if counter[s[i]] <= 0:
                    chars.remove(s[i])
                i += 1
            res = max(res, j - i)
        return res