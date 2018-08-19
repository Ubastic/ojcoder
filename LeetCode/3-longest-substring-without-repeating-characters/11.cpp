class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int chars[128] = {0};
        int beg = 0, end = 0;
        int maxlen = 0;
        for (; end < s.length(); end++) {
            chars[s[end]]++;
            while (beg < end && chars[s[end]] >= 2) {
                chars[s[beg]]--;
                beg++;
            }
            maxlen = max(maxlen, end-beg+1);
        }
        return maxlen;
    }
};
